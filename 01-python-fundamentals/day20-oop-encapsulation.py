"""
Day 20 - Python Fundamentals: OOP Encapsulation.

Topic: Encapsulation — bundling data (attributes) and the methods that operate
on that data into a single unit (a class), and restricting direct access to
some of the object's internal state.

This file teaches beginner-friendly encapsulation with a BankAccount example:

  1. What is encapsulation?
     - Hides internal data and exposes only controlled ways to read/change it.
     - Protects the object's state from invalid or accidental changes.

  2. Public, protected and private attributes
     - Public:    accessible from everywhere (e.g. account_holder_name).
     - Protected: _account_number  — by convention, "internal use only".
     - Private:   __balance        — Python name-mangles it so outside code
                cannot touch it by that name.

  3. Private variables using double underscores
     - __balance is stored as _BankAccount__balance inside the object.
     - Reading account.__balance from outside raises AttributeError.

  4. Getters and setters
     - Getter  (property balance): read __balance safely.
     - Setter  (balance = value):  change __balance only after validation.

  5. Why encapsulation is useful
     - Prevents negative deposits and withdrawals greater than the balance.
     - Centralizes all validation in one place (the class).
     - Lets us change the internal implementation without breaking callers.
"""

# ============================================================================
# Class: BankAccount
# ============================================================================


class BankAccount:
    """A simple bank account with encapsulated (protected) balance.

    The balance is private: it can only be changed through deposit() and
    withdraw(), which validate every operation.
    """

    def __init__(self, account_holder_name, account_number, initial_balance=0):
        """Initialize the account.

        Args:
            account_holder_name: Name of the account holder (public).
            account_number:      Account number (protected).
            initial_balance:     Starting balance (private, must be >= 0).

        Raises:
            ValueError: If initial_balance is negative.
        """
        # --- Public attribute: anyone can read or change it ---------------
        self.account_holder_name = account_holder_name

        # --- Protected attribute: by convention, internal use only --------
        # The single underscore _ is a hint to other programmers, not a hard
        # restriction. Code outside the class *can* still read it, but
        # should not.
        self._account_number = account_number

        # --- Private attribute: name-mangled by Python --------------------
        # Double underscore __ makes Python store it as _BankAccount__balance
        # so outside code cannot reach it by the name __balance.
        # We validate through the setter-like logic below.
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance
    # ------------------------------------------------------------------
    # Getter: read the private balance safely
    # ------------------------------------------------------------------
    @property
    def balance(self):
        """Return the current account balance.

        This is the getter. It lets callers read __balance without
        accessing the private attribute directly.
        """
        return self.__balance

    # ------------------------------------------------------------------
    # Setter: change the private balance only with validation
    # ------------------------------------------------------------------
    @balance.setter
    def balance(self, new_balance):
        """Set the balance only if the new value is valid (>= 0).

        This is the setter. It keeps the balance private and valid even
        when something tries to assign account.balance = ...
        """
        if new_balance < 0:
            raise ValueError("Balance cannot be set to a negative value.")
        self.__balance = new_balance

    # ------------------------------------------------------------------
    # Helper: read the protected account number (getter-style accessor)
    # ------------------------------------------------------------------
    def get_account_number(self):
        """Return the protected account number."""
        return self._account_number
    # ------------------------------------------------------------------
    # deposit: add money to the account
    # ------------------------------------------------------------------
    def deposit(self, amount):
        """Deposit money into the account.

        Args:
            amount: The amount to deposit (must be positive).

        Raises:
            ValueError: If amount is negative or zero.
        """
        # Prevent negative (and zero) deposits.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    # ------------------------------------------------------------------
    # withdraw: take money out of the account
    # ------------------------------------------------------------------
    def withdraw(self, amount):
        """Withdraw money from the account.

        Args:
            amount: The amount to withdraw (must be positive and <= balance).

        Raises:
            ValueError: If amount is negative/zero or greater than balance.
        """
        # Prevent negative or zero withdrawals.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        # Prevent withdrawals greater than the available balance (no overdraft).
        if amount > self.__balance:
            raise ValueError(
                f"Insufficient balance. Available: {self.__balance}, "
                f"requested: {amount}"
            )
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    # ------------------------------------------------------------------
    # display_balance: show the current balance
    # ------------------------------------------------------------------
    def display_balance(self):
        """Print the account holder's name and current balance."""
        print(f"Account holder: {self.account_holder_name}")
        print(f"Account number: {self.get_account_number()}")
        print(f"Current balance: {self.__balance}")


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 20 - Python Fundamentals: OOP Encapsulation (BankAccount)")
    print("=" * 60)
    print()

    # --- Create an account ----------------------------------------------
    print("--- Create account ---")
    account = BankAccount("Khalil", "ACC-1001", 1000)
    account.display_balance()
    print()

    # --- Public attribute: readable and writable ------------------------
    print("--- Public attribute (account_holder_name) ---")
    print(f"Holder: {account.account_holder_name}")
    account.account_holder_name = "Khalil Rahman"
    print(f"Updated holder: {account.account_holder_name}")
    print()

    # --- Protected attribute: readable (by convention, internal only) ---
    print("--- Protected attribute (_account_number) ---")
    print(f"Account number: {account.get_account_number()}")
    print()

    # --- Private attribute: NOT directly accessible ---------------------
    print("--- Private attribute (__balance) ---")
    try:
        print(account.__balance)
    except AttributeError as error:
        print(f"account.__balance -> AttributeError: {error}")
    # Name-mangled access works but is discouraged (shows it is "private").
    print(f"Via name mangling (_BankAccount__balance): {account._BankAccount__balance}")
    print()

    # --- Getter (property balance) --------------------------------------
    print("--- Getter: account.balance ---")
    print(f"Balance: {account.balance}")
    print()

    # --- Setter (property balance) --------------------------------------
    print("--- Setter: account.balance = 2000 ---")
    try:
        account.balance = 2000
        print(f"Balance after set: {account.balance}")
    except ValueError as error:
        print(f"Setter rejected: {error}")
    print()

    # --- Deposit --------------------------------------------------------
    print("--- Deposit 500 ---")
    account.deposit(500)
    print()

    # --- Prevent negative deposit ---------------------------------------
    print("--- Prevent negative deposit (-100) ---")
    try:
        account.deposit(-100)
    except ValueError as error:
        print(f"deposit(-100) -> ValueError: {error}")
    print()

    # --- Withdrawal -----------------------------------------------------
    print("--- Withdraw 300 ---")
    account.withdraw(300)
    print()

    # --- Prevent overdraft ----------------------------------------------
    print("--- Prevent overdraft (withdraw 100000) ---")
    try:
        account.withdraw(100000)
    except ValueError as error:
        print(f"withdraw(100000) -> ValueError: {error}")
    print()

    # --- Final state ----------------------------------------------------
    print("--- Final account state ---")
    account.display_balance()
    print()

    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()