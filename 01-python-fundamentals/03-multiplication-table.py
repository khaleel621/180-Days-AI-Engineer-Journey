"""Day 2 Exercise: Print a multiplication table from 1 to 10."""

def multiplication_table(number):
    """Build the multiplication table for number from 1 through 10."""
    lines = []
    for multiplier in range(1, 11):
        lines.append(f"{number} x {multiplier} = {number * multiplier}")
    return lines


def main():
    table_number = int(input("Enter an integer for its multiplication table: "))
    print(f"Multiplication table for {table_number}:")
    for line in multiplication_table(table_number):
        print(line)


if __name__ == "__main__":
    main()