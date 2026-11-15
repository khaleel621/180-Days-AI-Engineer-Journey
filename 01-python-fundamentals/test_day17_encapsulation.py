"""
Tests for Day 17 - Encapsulation and Access Modifiers in
01-python-fundamentals/day17-encapsulation.py.

Covers:
  - BankAccount: public, protected and private attributes.
  - deposit() and withdraw() with valid and invalid amounts.
  - get_balance() getter for the private balance.
  - get_account_holder_name() / set_account_holder_name() getter and setter.
  - Invalid input raises ValueError; insufficient funds raises ValueError.
  - Private balance is not directly accessible from outside the class.
  - Object independence.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day17-encapsulation.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day17-encapsulation.py")
_spec = importlib.util.spec_from_file_location("day17_encapsulation", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

BankAccount = _module.BankAccount


def test_account_stores_name_number_and_initial_balance():
    account = BankAccount("Ada Lovelace", "ACC-1001", 500)
    assert account.account_holder_name == "Ada Lovelace"
    assert account._account_number == "ACC-1001"
    assert account.get_balance() == 500


def test_account_holder_name_is_public():
    account = BankAccount("Ben", "ACC-1002")
    account.account_holder_name = "Benjamin"
    assert account.account_holder_name == "Benjamin"


def test_default_initial_balance_is_zero():
    account = BankAccount("Cid", "ACC-1003")
    assert account.get_balance() == 0


def test_deposit_adds_to_balance():
    account = BankAccount("Ada", "ACC-1001", 100)
    account.deposit(250)
    assert account.get_balance() == 350


def test_deposit_invalid_amounts_raise_value_error():
    account = BankAccount("Ada", "ACC-1001")
    for invalid_amount in [0, -10, -0.01, "100", None, True]:
        try:
            account.deposit(invalid_amount)
        except ValueError:
            pass
        else:
            raise AssertionError(f"deposit({invalid_amount!r}) did not raise ValueError")


def test_withdraw_subtracts_from_balance():
    account = BankAccount("Ben", "ACC-1002", 500)
    account.withdraw(120)
    assert account.get_balance() == 380


def test_withdraw_invalid_amounts_raise_value_error():
    account = BankAccount("Ben", "ACC-1002", 500)
    for invalid_amount in [0, -20, "50", None, False]:
        try:
            account.withdraw(invalid_amount)
        except ValueError:
            pass
        else:
            raise AssertionError(f"withdraw({invalid_amount!r}) did not raise ValueError")


def test_withdraw_more_than_balance_raises_value_error():
    account = BankAccount("Cid", "ACC-1003", 100)
    try:
        account.withdraw(10000)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "withdraw(10000) with balance 100 did not raise ValueError"
        )
    assert account.get_balance() == 100  # unchanged after the failed withdrawal


def test_get_account_holder_name_getter():
    account = BankAccount("Ada", "ACC-1001")
    assert account.get_account_holder_name() == "Ada"


def test_set_account_holder_name_setter():
    account = BankAccount("Ben", "ACC-1002")
    account.set_account_holder_name("Benjamin")
    assert account.get_account_holder_name() == "Benjamin"
    assert account.account_holder_name == "Benjamin"


def test_set_account_holder_name_invalid_raises_value_error():
    account = BankAccount("Cid", "ACC-1003")
    for invalid_name in ["", "   ", None, 123]:
        try:
            account.set_account_holder_name(invalid_name)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"set_account_holder_name({invalid_name!r}) did not raise ValueError"
            )


def test_private_balance_not_accessible_directly():
    account = BankAccount("Ada", "ACC-1001", 500)
    try:
        account.__balance
    except AttributeError:
        pass
    else:
        raise AssertionError("account.__balance did not raise AttributeError")
    # The getter still works.
    assert account.get_balance() == 500


def test_protected_account_number_accessible_by_convention():
    account = BankAccount("Ben", "ACC-1002")
    assert account._account_number == "ACC-1002"


def test_two_accounts_are_independent():
    account1 = BankAccount("Ada", "ACC-1001", 500)
    account2 = BankAccount("Ben", "ACC-1002", 300)
    account1.withdraw(200)
    assert account2.get_balance() == 300  # account2 unaffected


if __name__ == "__main__":
    test_account_stores_name_number_and_initial_balance()
    test_account_holder_name_is_public()
    test_default_initial_balance_is_zero()
    test_deposit_adds_to_balance()
    test_deposit_invalid_amounts_raise_value_error()
    test_withdraw_subtracts_from_balance()
    test_withdraw_invalid_amounts_raise_value_error()
    test_withdraw_more_than_balance_raises_value_error()
    test_get_account_holder_name_getter()
    test_set_account_holder_name_setter()
    test_set_account_holder_name_invalid_raises_value_error()
    test_private_balance_not_accessible_directly()
    test_protected_account_number_accessible_by_convention()
    test_two_accounts_are_independent()
    print("All test_day17_encapsulation tests passed!")