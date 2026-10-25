"""Day 2 DSA Exercise: Count even numbers in a list using a loop and counter."""

def count_even_numbers(numbers):
    """Count even values with a for loop, if condition, and counter.

    Does not use the built-in list.count() method.
    """
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count


def main():
    numbers = [12, 7, 4, 9, 6, 3, 8]
    print(f"Even numbers count: {count_even_numbers(numbers)}")


if __name__ == "__main__":
    main()