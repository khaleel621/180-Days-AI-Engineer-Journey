"""Day 2 Exercise: Check whether an integer is even or odd."""

def even_or_odd(number):
    """Return a clear even/odd message for an integer, including zero/negatives."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    number = int(input("Enter an integer to check: "))
    print(even_or_odd(number))


if __name__ == "__main__":
    main()