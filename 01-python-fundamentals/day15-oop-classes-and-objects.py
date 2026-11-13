"""
Day 15 - Python Fundamentals: Object-Oriented Programming — Classes and Objects.

Topic: Classes and Objects

This file teaches beginner-friendly object-oriented programming with two
classes:

  1. Student(name, marks)
     - Stores the student's name and marks.
     - display_details() prints the student's name and marks.
     - is_passed() returns True when marks are at least 40, otherwise False.

  2. BankAccount(owner, balance)
     - Stores the account owner and the current balance.
     - deposit(amount) adds a positive amount to the balance.
     - withdraw(amount) removes the amount when enough balance exists.
     - get_balance() returns the current balance.

Each object keeps its own data: changing one student or one bank account never
affects another object.

Error-handling behaviour (chosen and documented):
  - Invalid input raises ValueError with a clear message instead of silently
    doing the wrong thing.
  - Student: name must be a non-empty string; marks must be a number between
    0 and 100 inclusive.
  - BankAccount: owner must be a non-empty string; starting balance must be a
    non-negative number.
  - deposit() and withdraw() accept only positive numbers.
  - withdraw() rejects amounts larger than the balance and leaves the balance
    unchanged.
"""

# ============================================================================
# Class 1: Student
# ============================================================================


class Student:
    """A student with a name and marks."""

    def __init__(self, name, marks):
        """Initialize a Student with a name and marks.

        Args:
            name: The student's name (must be a non-empty string).
            marks: The student's marks (must be a number between 0 and 100).

        Raises:
            ValueError: If name is empty or marks are not a number in 0..100.
        """
        # Validate the name: it must be a string and not empty or whitespace only.
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")

        # Validate marks: must be a real number (bool is not accepted) in 0..100.
        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        # Each object stores its own name and marks (instance attributes).
        self.name = name
        self.marks = marks

    def display_details(self):
        """Display the student's name and marks."""
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        """Return True if marks are at least 40, otherwise False.

        Returns:
            True when self.marks >= 40, False otherwise.
        """
        return self.marks >= 40


# ============================================================================
# Class 2: BankAccount
# ============================================================================


class BankAccount:
    """A simple bank account with an owner and a balance."""

    def __init__(self, owner, balance):
        """Initialize a BankAccount with an owner and a starting balance.

        Args:
            owner: The account owner's name (non-empty string).
            balance: The starting balance (non-negative number).

        Raises:
            ValueError: If owner is empty or balance is negative.
        """
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Account owner must be a non-empty string.")
        if isinstance(balance, bool) or not isinstance(balance, (int, float)):
            raise ValueError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Starting balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account.

        Args:
            amount: The amount to deposit (must be a positive number).

        Raises:
            ValueError: If amount is not a positive number.
        """
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    def withdraw(self, amount):
        """Withdraw an amount when sufficient balance exists.

        Args:
            amount: The amount to withdraw (positive and not more than the
                current balance).

        Raises:
            ValueError: If amount is not a positive number or exceeds the
                balance. The balance is left unchanged when the withdrawal is
                rejected.
        """
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for this withdrawal.")

        self.balance -= amount

    def get_balance(self):
        """Return the current account balance."""
        return self.balance


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 15 - Python Fundamentals: Classes and Objects")
    print("=" * 60)
    print()

    # --- Student examples ---------------------------------------------------
    print("--- Student class ---")
    student1 = Student("Ada", 85)
    student2 = Student("Ben", 35)

    student1.display_details()
    print(f"Passed: {student1.is_passed()}")   # True (85 >= 40)
    print()
    student2.display_details()
    print(f"Passed: {student2.is_passed()}")   # False (35 < 40)
    print()

    # --- BankAccount examples ----------------------------------------------
    print("--- BankAccount class ---")
    account1 = BankAccount("Ada", 100)
    account2 = BankAccount("Ben", 50)

    print(f"{account1.owner}'s balance: {account1.get_balance()}")  # 100
    account1.deposit(25)
    print(f"After depositing 25: {account1.get_balance()}")          # 125
    account1.withdraw(40)
    print(f"After withdrawing 40: {account1.get_balance()}")         # 85

    # account2 is independent of account1.
    print(f"{account2.owner}'s balance: {account2.get_balance()}")  # 50

    # Rejected transactions leave the balance unchanged.
    try:
        account1.withdraw(1000)
    except ValueError as error:
        print(f"Withdrawal rejected: {error}")
    print(f"{account1.owner}'s balance after rejected withdrawal: {account1.get_balance()}")  # 85

    try:
        account1.deposit(-10)
    except ValueError as error:
        print(f"Deposit rejected: {error}")

    print()
    print("=" * 60)
    print("Demo complete. Objects keep their own data.")
    print("=" * 60)


if __name__ == "__main__":
    main()