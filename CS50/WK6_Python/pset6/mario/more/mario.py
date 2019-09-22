# Build a Mario pyramid with a height equal to an user inputted integer
from cs50 import get_int

# Ask user for height
while True:
    h = get_int("Height: ")
    if h > 0 and h < 9:
        break

# Print pyramid
for i in range(h):
    print(" " * (h - i - 1), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))

