"""
Tests for Day 20 - OOP Encapsulation in
01-python-fundamentals/day20-oop-encapsulation.py.

Covers:
  - Public attribute account_holder_name is readable/writable.
  - Protected attribute _account_number is accessible by convention.
  - Private attribute __balance is NOT directly accessible (AttributeError)
    and is reachable only via name mangling (_BankAccount__balance).
  - Getter: account.balance returns the private balance.
  - Setter: account.balance = value validates and updates the balance.
  - deposit() adds money and rejects negative/zero amounts.
  - withdraw() removes money and rejects overdrafts and invalid amounts.
  - display_balance() prints holder, account number and balance.
  - Initial negative balance raises ValueError.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day20-oop-encapsulation.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day20-oop-encapsulation.py")
_spec = importlib.util.spec_from_file_location("day20_oop_encapsulation", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

BankAccount = _module.BankAccount


def _make_account(balance=1000):
    return BankAccount("Khalil", "ACC-1001", balance)


# -----------------------------------------------------------
# Public / protected / private attributes
# -----------------------------------------------------------

def test_account_holder_name_is_public():
    """account_holder_name is public: readable and writable."""
    account = _make_account()
    assert account.account_holder_name == "Khalil"
    account.account_holder_name = "Khalil Rahman"
    assert account.account_holder_name == "Khalil Rahman"


def test_account_number_is_protected():
    """_account_number is protected: accessible via accessor (convention)."""
    account = _make_account()
    assert account.get_account_number() == "ACC-1001"
    # Protected members are still reachable (a hint, not a hard block).
    assert account._account_number == "ACC-1001"


def test_balance_is_private_not_directly_accessible():
    """__balance is private: direct access raises AttributeError."""
    account = _make_account()
    try:
        account.__balance
    except AttributeError:
        pass
    else:
        raise AssertionError("account.__balance did not raise AttributeError")


def test_balance_is_private_reachable_via_name_mangling():
    """__balance is stored as _BankAccount__balance (name mangling)."""
    account = _make_account(500)
    assert account._BankAccount__balance == 500


# -----------------------------------------------------------
# Getter and setter
# -----------------------------------------------------------

def test_get_balance_getter():
    """The balance getter returns the private balance."""
    account = _make_account(750)
    assert account.balance == 750


def test_set_balance_setter_valid():
    """The balance setter accepts a valid non-negative value."""
    account = _make_account()
    account.balance = 2000
    assert account.balance == 2000


def test_set_balance_setter_rejects_negative():
    """The balance setter rejects negative values."""
    account = _make_account()
    try:
        account.balance = -100
    except ValueError:
        pass
    else:
        raise AssertionError("account.balance = -100 did not raise ValueError")
    # Balance must be unchanged after a rejected assignment.
    assert account.balance == 1000


# -----------------------------------------------------------
# deposit
# -----------------------------------------------------------

def test_deposit_positive_amount():
    """deposit(amount) increases the balance."""
    account = _make_account(1000)
    account.deposit(500)
    assert account.balance == 1500


def test_deposit_negative_amount_raises():
    """deposit() rejects a negative amount."""
    account = _make_account(1000)
    try:
        account.deposit(-100)
    except ValueError:
        pass
    else:
        raise AssertionError("deposit(-100) did not raise ValueError")
    assert account.balance == 1000


def test_deposit_zero_raises():
    """deposit() rejects a zero deposit (not positive)."""
    account = _make_account(1000)
    try:
        account.deposit(0)
    except ValueError:
        pass
    else:
        raise AssertionError("deposit(0) did not raise ValueError")
    assert account.balance == 1000


# -----------------------------------------------------------
# withdraw
# -----------------------------------------------------------

def test_withdraw_valid_amount():
    """withdraw(amount) decreases the balance."""
    account = _make_account(1000)
    account.withdraw(300)
    assert account.balance == 700


def test_withdraw_entire_balance():
    """withdraw() can take the full balance, leaving zero."""
    account = _make_account(500)
    account.withdraw(500)
    assert account.balance == 0


def test_withdraw_negative_amount_raises():
    """withdraw() rejects a negative amount."""
    account = _make_account(1000)
    try:
        account.withdraw(-50)
    except ValueError:
        pass
    else:
        raise AssertionError("withdraw(-50) did not raise ValueError")
    assert account.balance == 1000


def test_withdraw_zero_raises():
    """withdraw() rejects a zero withdrawal."""
    account = _make_account(1000)
    try:
        account.withdraw(0)
    except ValueError:
        pass
    else:
        raise AssertionError("withdraw(0) did not raise ValueError")
    assert account.balance == 1000


def test_withdraw_greater_than_balance_raises():
    """withdraw() rejects overdrafts (amount > balance)."""
    account = _make_account(100)
    try:
        account.withdraw(100000)
    except ValueError:
        pass
    else:
        raise AssertionError("withdraw(100000) did not raise ValueError")
    assert account.balance == 100


# -----------------------------------------------------------
# Initial balance validation
# -----------------------------------------------------------

def test_initial_negative_balance_raises():
    """Creating an account with a negative balance raises ValueError."""
    try:
        BankAccount("Khalil", "ACC-1001", -500)
    except ValueError:
        pass
    else:
        raise AssertionError("BankAccount(..., -500) did not raise ValueError")


# -----------------------------------------------------------
# display_balance
# -----------------------------------------------------------

def test_display_balance_runs_without_error():
    """display_balance() should execute without raising."""
    account = _make_account(1234)
    # Simply calling it must not raise; it prints to stdout.
    account.display_balance()
    assert account.balance == 1234


if __name__ == "__main__":
    test_account_holder_name_is_public()
    test_account_number_is_protected()
    test_balance_is_private_not_directly_accessible()
    test_balance_is_private_reachable_via_name_mangling()
    test_get_balance_getter()
    test_set_balance_setter_valid()
    test_set_balance_setter_rejects_negative()
    test_deposit_positive_amount()
    test_deposit_negative_amount_raises()
    test_deposit_zero_raises()
    test_withdraw_valid_amount()
    test_withdraw_entire_balance()
    test_withdraw_negative_amount_raises()
    test_withdraw_zero_raises()
    test_withdraw_greater_than_balance_raises()
    test_initial_negative_balance_raises()
    test_display_balance_runs_without_error()
    print("All test_day20_oop_encapsulation tests passed!")