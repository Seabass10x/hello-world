from cs50 import get_string
from sys import argv, exit


def main():

    # Check that a banned list was submitted as an argument
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # Open dictionary of banned words
    banfile = open(argv[1])
    banned = set()

    # Add banned words to set
    for word in banfile:
        banned.add(word.rstrip())

    # Get message from User and put words in a list
    message = get_string("What message would you like to censor?\n")
    words = message.strip().split()

    # Iterate through words in message
    for word in words:

        # Bleep out banned words
        if word.lower() in banned:
            wdlen = len(word)
            print("*" * wdlen, end=" ")
        else:
            print(f"{word} ", end="")
    print()


if __name__ == "__main__":
    main()
