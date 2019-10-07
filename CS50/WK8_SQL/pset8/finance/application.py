import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Select stock symbols and the sums of their shares
    portfolio = db.execute("SELECT symbol, SUM(shares) FROM transactions GROUP BY symbol HAVING user_id = :userid AND SUM(shares) > 0 ORDER BY symbol",
                           userid=session["user_id"])

    # Select the ampount of cash a user has
    cash = db.execute("SELECT cash FROM users WHERE id = :userid", userid=session["user_id"])

    # Declare a var for grand total
    grandtotal = cash[0]["cash"]

    # Look up stock info and calculate total value of holding
    for stock in portfolio:
        info = lookup(stock["symbol"])
        stock.update(info)
        total = stock["SUM(shares)"] * stock["price"]
        grandtotal += total
        stock["price"] = usd(stock["price"])
        stock.update({"total": usd(total)})

    # Add cash value to portfolio
    portfolio.append({"symbol": "cash", "name": "US Dollar", "total": usd(cash[0]["cash"])})

    return render_template("index.html", portfolio=portfolio, grandtotal=usd(grandtotal))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("symbol"):
            return apology("must provide a stock symbol", 403)

        # Ensure # of shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide # of shares", 403)

        # Convert input # of shares to an integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("# of shares must be a positive integer", 400)

        # Ensure # of shares is a positive integer
        if shares < 1:
            return apology("# of shares must be a positive integer", 400)

        # Look up the stock via api
        stock = lookup(request.form.get("symbol"))

        # Ensure the input symbol is valid
        if not stock:
            return apology("stock symbol is not valid", 400)

        # Look up available funds
        cash = db.execute("SELECT cash FROM users WHERE id = :userid", userid=session["user_id"])
        cash = float(cash[0]['cash'])
        cost = stock["price"] * shares

        # Check for NSF
        if (cash - cost) < 0:
            return apology("insufficient funds", 403)

        # Insert buy order into transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, amount) VALUES (:userid, :symbol, :shares, :cost)",
                   userid=session["user_id"], symbol=stock["symbol"], shares=shares, cost=cost)

        # Update available cash on users table
        db.execute("UPDATE users SET cash = :cash WHERE id = :userid", cash=(cash - cost), userid=session["user_id"])

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    username = request.args.get("username")
    if len(username) > 0 and len(db.execute("SELECT * FROM users WHERE username = :username", username=username)) == 0:
        return jsonify(True)
    else:
        return jsonify(False)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Select all transaction for the current user
    transactions = db.execute("SELECT timestamp, symbol, shares, amount FROM transactions WHERE user_id = :userid ORDER BY timestamp",
                              userid=session["user_id"])

    # Format each transaction for History Table
    for transaction in transactions:

        # Determine if a txn is a BUY or SELL
        if transaction["shares"] < 0:
            txn = {"TXN": "SELL"}
            transaction.update(txn)
        else:
            txn = {"TXN": "BUY"}
            transaction.update(txn)

        transaction["shares"] = abs(transaction["shares"])
        transaction["amount"] = usd(abs(transaction["amount"]))

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by clicking the Quote button)
    if request.method == "POST":

        # Ensure a stock symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide a stock symbol", 400)

        # Look up price of stock
        stock = lookup(request.form.get("symbol"))

        # Ensure the input symbol is valid
        if not stock:
            return apology("stock symbol is not valid", 400)

        stock["price"] = usd(stock["price"])

        # Render table of quoted stock
        return render_template("quoted.html", stock=stock)

    # User reached route via GET (as by clicking the Quote link)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by clicking on Register button)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 0:
            return apology("username is not available", 400)

        # Hash the password
        pwhash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        # Write username and hash to db
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :pwhash)",
                   username=request.form.get("username"), pwhash=pwhash)

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking on Register)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by clicking the Sell button)
    if request.method == "POST":

        # Ensure a stock symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide a stock symbol", 400)

        # Ensure # of shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide # of shares", 400)

        # Select the SUM of shares owned of input stock
        owned_shares = db.execute("SELECT SUM(shares) FROM transactions WHERE symbol = :symbol AND user_id = :userid",
                                  symbol=request.form.get("symbol"), userid=session["user_id"])
        owned_shares = int(owned_shares[0]["SUM(shares)"])

        # Convert input # of shares to an integer
        try:
            sold_shares = int(request.form.get("shares"))
        except:
            return apology("# of shares must be a positive integer", 400)

        # Ensure that user owns shares of input stock
        if owned_shares < 1:
            return apology("you don't own any of these shares", 400)

        # Ensure user is trying to sell a positive integer of share
        elif sold_shares < 1:
            return apology("# of shares must be a positive integer", 400)

        # Ensure user owns at least the number of shares they are selling
        elif owned_shares < sold_shares:
            return apology("you can not sell more shares than you own", 400)

        stock = lookup(request.form.get("symbol"))
        minus_shares = -sold_shares
        amount = stock["price"] * minus_shares

        # Add sell order to transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, amount) VALUES (:userid, :symbol, :shares, :amount)",
                   userid=session["user_id"], symbol=stock["symbol"], shares=minus_shares, amount=amount)

        # Update available cash on users table
        cash = db.execute("SELECT cash FROM users WHERE id = :userid", userid=session["user_id"])
        cash = float(cash[0]["cash"])
        db.execute("UPDATE users SET cash = :cash WHERE id = :userid", cash=(cash - amount), userid=session["user_id"])

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Select a user's stocks
        stocks = db.execute("SELECT symbol FROM transactions GROUP BY symbol HAVING user_id = :userid AND SUM(shares) > 0 ORDER BY symbol",
                            userid=session["user_id"])

        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
