# Find PI to the Nth Digit
#   Enter a number and have the program generate PI up to that many decimal places.
#   Keep a limit to how far the program will go.
import math
from decimal import Decimal


def trim_pi(n):
    pi = Decimal.from_float(math.pi)
    num = str(pi)
    digits = num.split('.')
    string = digits[0] + '.' + str(digits[1])[:n]
    return string


def main():
    x = False
    while not x:
        n = int(input("Enter a number and have the program generate PI up to that many decimal places: "))
        if n > 200:
            print("Value is too large, please enter a smaller value")
        else:
            x = True

    print("Pi to the", n, "decimal is", trim_pi(n))


if __name__ == "__main__":
    main()