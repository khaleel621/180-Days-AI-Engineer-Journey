"""
Day 17 - Python Fundamentals: OOP Encapsulation and Access Modifiers.

Topic: Encapsulation — public, protected and private attributes, getters and setters.

This file teaches beginner-friendly encapsulation with a practical Bank Account example:

  1. Encapsulation
     - Bundling data (attributes) and the operations on that data (methods) into one class.
     - Hiding the internal state so outside code cannot change it directly or by accident.

  2. Public attributes
     - Written as normal names, e.g. self.account_holder_name.
     - Anyone can read or write them from outside the class.

  3. Protected attributes
     - Written with a single leading underscore, e.g. self._account_number.
     - A convention: "internal use, please do not touch from outside".
     - Python does NOT block access; it is only a hint to other programmers.

  4. Private attributes
     - Written with a double leading underscore, e.g. self.__balance.
     - Python applies "name mangling": __balance becomes _BankAccount__balance.
     - Direct access from outside the class (account.__balance) raises AttributeError.
     - It is still possible via _BankAccount__balance, but that breaks encapsulation on purpose.

  5. Getters and setters
     - Getter: a method that returns a hidden attribute (get_balance()).
     - Setter: a method that changes a hidden attribute after validating the new value
       (set_account_holder_name()).
     - They let the class control how its data is read and changed.

  6. Practical Bank Account example
     - BankAccount(account_holder_name, account_number, initial_balance=0)
     - deposit(amount) adds money after validating the amount.
     - withdraw(amount) removes money after validating the amount and sufficient funds.
     - get_balance() returns the private balance.
     - Invalid amounts (zero, negative, text, None, True/False) raise ValueError.

Error-handling behaviour (chosen and documented):
  - All invalid input raises ValueError with a clear message.
  - Deposit and withdrawal amounts must be real numbers (bool is rejected) and greater than zero.
  - A withdrawal cannot exceed the current balance (insufficient funds -> ValueError).
  - The account holder name must be a non-empty string.
"""

# ============================================================================
# BankAccount class
# ============================================================================


class BankAccount:
    """A simple bank account demonstrating encapsulation and access modifiers."""

    def __init__(self, account_holder_name, account_number, initial_balance=0):
        """Initialize a bank account.

        Args:
            account_holder_name: Name of the account holder (non-empty string).
            account_number: The account number (non-empty string).
            initial_balance: Starting balance (zero or a positive number).

        Raises:
            ValueError: If the name is empty or the initial balance is invalid.
        """
        # --- Public attribute ------------------------------------------------
        # No leading underscore: anyone can read or write it directly.
        # The setter is used so the name is validated right away.
        self.set_account_holder_name(account_holder_name)

        # --- Protected attribute --------------------------------------------
        # Single leading underscore: "internal use" by convention.
        # Python still allows reading and writing it from outside the class.
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Account number must be a non-empty string.")
        self._account_number = account_number.strip()

        # --- Private attribute ----------------------------------------------
        # Double leading underscore: name-mangled so outside code cannot reach
        # it as account.__balance. Starts at zero; use deposit() to add money.
        self.__balance = 0

        # Validate the initial balance: must be a real number (bool rejected)
        # and must not be negative. Zero is allowed for a new account.
        if isinstance(initial_balance, bool) or not isinstance(
            initial_balance, (int, float)
        ):
            raise ValueError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = float(initial_balance)

    # ------------------------------------------------------------------
    # Getter and setter for the public account holder name
    # ------------------------------------------------------------------

    def get_account_holder_name(self):
        """Return the account holder's name."""
        return self.account_holder_name

    def set_account_holder_name(self, new_name):
        """Change the account holder's name after validating it.

        Raises:
            ValueError: If new_name is not a non-empty string.
        """
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Account holder name must be a non-empty string.")
        self.account_holder_name = new_name.strip()

    # ------------------------------------------------------------------
    # Protected attribute accessor
    # ------------------------------------------------------------------

    def get_account_number(self):
        """Return the account number (protected attribute)."""
        return self._account_number

    # ------------------------------------------------------------------
    # Private attribute getter
    # ------------------------------------------------------------------

    def get_balance(self):
        """Return the current balance.

        Returns:
            The private balance as a number. This is the getter for the
            private __balance attribute. (Python also offers the @property
            decorator for this; an explicit getter is shown here because it
            is beginner-friendly and explicit.)
        """
        return self.__balance

    # ------------------------------------------------------------------
    # Deposit and withdrawal
    # ------------------------------------------------------------------

    def _validate_amount(self, amount, operation):
        """Check that an amount is a positive real number.

        Raises:
            ValueError: If amount is not a number (bool is rejected) or is
                zero or negative.
        """
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError(f"{operation} amount must be a number.")
        if amount <= 0:
            raise ValueError(f"{operation} amount must be greater than zero.")

    def deposit(self, amount):
        """Deposit money into the account.

        Args:
            amount: The amount to deposit (must be a positive number).

        Raises:
            ValueError: If the amount is invalid.
        """
        self._validate_amount(amount, "Deposit")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        """Withdraw money from the account.

        Args:
            amount: The amount to withdraw (must be a positive number and
                not more than the current balance).

        Raises:
            ValueError: If the amount is invalid or exceeds the balance.
        """
        self._validate_amount(amount, "Withdrawal")
        if amount > self.__balance:
            raise ValueError(
                f"Insufficient funds: balance is {self.__balance}, "
                f"requested {amount}."
            )
        self.__balance -= amount


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 17 - Python Fundamentals: OOP Encapsulation and Access Modifiers")
    print("=" * 60)
    print()

    # --- Create an account ------------------------------------------------
    print("--- Creating a bank account ---")
    account = BankAccount("Ada Lovelace", "ACC-1001", 500)
    print(f"Holder (public):   {account.get_account_holder_name()}")
    print(f"Account number:    {account.get_account_number()}")
    print(f"Balance:           {account.get_balance()}")
    print()

    # --- Public attribute: can be read and changed directly ---------------
    print("--- Public attribute (account_holder_name) ---")
    print(f"Direct read: {account.account_holder_name}")
    account.account_holder_name = "Ada King"
    print(f"After direct change: {account.account_holder_name}")
    account.set_account_holder_name("Ada Lovelace")
    print(f"After validated setter: {account.get_account_holder_name()}")
    print()

    # --- Deposit and withdrawal -------------------------------------------
    print("--- Deposit and withdrawal ---")
    account.deposit(250)
    print(f"Deposited 250. Balance: {account.get_balance()}")  # 750.0
    account.withdraw(100)
    print(f"Withdrew 100. Balance: {account.get_balance()}")  # 650.0
    print()

    # --- Validation: invalid deposit and withdrawal amounts ---------------
    print("--- Invalid deposit/withdrawal amounts ---")
    for label, action in [
        ("deposit(0)", lambda: account.deposit(0)),
        ("deposit(-10)", lambda: account.deposit(-10)),
        ("deposit('100')", lambda: account.deposit("100")),
        ("deposit(None)", lambda: account.deposit(None)),
        ("deposit(True)", lambda: account.deposit(True)),
        ("withdraw(0)", lambda: account.withdraw(0)),
        ("withdraw(-20)", lambda: account.withdraw(-20)),
        ("withdraw('50')", lambda: account.withdraw("50")),
    ]:
        try:
            action()
        except ValueError as error:
            print(f"{label}: rejected - {error}")
    print()

    # --- Insufficient funds -----------------------------------------------
    print("--- Withdrawal exceeding the balance ---")
    try:
        account.withdraw(10000)
    except ValueError as error:
        print(f"withdraw(10000): rejected - {error}")
    print(f"Balance unchanged: {account.get_balance()}")
    print()

    # --- Private attribute: direct access is blocked ----------------------
    print("--- Private attribute (__balance) ---")
    try:
        print(account.__balance)
    except AttributeError as error:
        print(f"account.__balance -> AttributeError: {error}")
    print("Name-mangled access (discouraged, breaks encapsulation):")
    print(f"  account._BankAccount__balance = {account._BankAccount__balance}")
    print()

    # --- Protected attribute: convention, not a block ---------------------
    print("--- Protected attribute (_account_number) ---")
    print(f"Accessible by convention: {account._account_number}")
    print()

    # --- Object independence ----------------------------------------------
    print("--- Object independence ---")
    account2 = BankAccount("Ben", "ACC-1002", 0)
    account2.deposit(300)
    print(f"{account.get_account_holder_name()}'s balance:  {account.get_balance()}")
    print(f"{account2.get_account_holder_name()}'s balance: {account2.get_balance()}")
    print()

    print("=" * 60)
    print("Demo complete. Encapsulation keeps the balance safe inside the class.")
    print("=" * 60)


if __name__ == "__main__":
    main()
