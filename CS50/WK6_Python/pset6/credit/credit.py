# Validates a credit card number using Luhn's Algorithm
from cs50 import get_int

# Have user input cc number
cc = get_int("Number: ")

# Convert cc to string and find length
cc = str(cc)
cclen = len(cc)

# Validate length
if cclen != 13 and cclen != 15 and cclen != 16:
    print("INVALID\n")
    quit()

# Reverse order of cc number
ccrev = "".join(reversed(cc))

# Place cc digits in list according to Luhn's Algorithm
evens = list()
odds = list()
for i in range(cclen):
    n = int(ccrev[i])
    if i % 2 == 0:
        evens.append(n)
    else:
        n = ((2 * n) // 10) + ((2 * n) % 10)
        odds.append(n)

# Perform checksum operation
chksum = (sum(evens) + sum(odds)) % 10

# Validate cc number based on format and checksum results
if chksum != 0:
    print("INVALID\n")
    quit()
if cclen == 13 and cc[0] == '4':
    print("VISA\n")
    quit()
if cclen == 15 and (cc[:2] == '34' or cc[:2] == '37'):
    print("AMEX\n")
    quit()
if cclen == 16 and cc[0] == '4':
    print("VISA\n")
    quit()
if cclen == 16 and int(cc[:2]) > 50 and int(cc[:2]) < 56:
    print("MASTERCARD\n")
    quit()
print("INVALID\n")
