# Crack a hashed password using brute force
from sys import argv
from crypt import crypt

# Check that a hash was submitted as an argument
if len(argv) != 2:
    print("Usage: python crack.py hash")
    quit()

# Assign variables
hash = argv[1]
salt = hash[:2]

# Possible elements of password arranged by most frequently used per http://letterfrequency.org/
alphabet = " EeTtAaOoIiNnSsRrHhLlDdCcUuMmFfPpGgWwYyBbVvKkXxJjQqZz"

# Iterate through all possible password combinations
for letter5 in alphabet:
    for letter4 in alphabet:
        for letter3 in alphabet:
            for letter2 in alphabet:
                for letter1 in alphabet[1:]:
                    password = f"{letter1}{letter2}{letter3}{letter4}{letter5}".strip()

                    # Compare each hashed password against the inputted hash
                    if crypt(password, salt) == hash:
                        print(password)
                        quit()
