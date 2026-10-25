"""Day 2 practice: conditions, loops, and a simple counting problem."""


def even_or_odd(number):
    """Return a clear even/odd message for an integer, including zero/negatives."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def multiplication_table(number):
    """Build the multiplication table for number from 1 through 10."""
    lines = []
    for multiplier in range(1, 11):
        lines.append(f"{number} x {multiplier} = {number * multiplier}")
    return lines


def count_even_numbers(numbers):
    """Count even values with a for loop, if condition, and counter."""
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count


def main():
    """Run each Day 2 exercise with values entered by the user."""
    number = int(input("Enter an integer to check: "))
    print(even_or_odd(number))

    table_number = int(input("Enter an integer for its multiplication table: "))
    print(f"Multiplication table for {table_number}:")
    for line in multiplication_table(table_number):
        print(line)

    numbers = [12, 7, 4, 9, 6, 3, 8]
    print(f"Even numbers count: {count_even_numbers(numbers)}")


if __name__ == "__main__":
    main()
