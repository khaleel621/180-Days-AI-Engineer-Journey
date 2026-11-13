"""
Tests for Day 15 - Classes and Objects in
01-python-fundamentals/day15-oop-classes-and-objects.py.

Covers:
  - Student: storing name/marks, display_details, is_passed (>= 40 passes),
    invalid name/marks (ValueError), and independence of objects.
  - BankAccount: storing owner/balance, get_balance, deposits, successful
    withdrawals, insufficient balance rejection, invalid transaction amounts,
    negative starting balance, and independence of accounts.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import contextlib
import io
import importlib.util
import os

# Load day15-oop-classes-and-objects.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day15-oop-classes-and-objects.py")
_spec = importlib.util.spec_from_file_location("day15_oop_classes_and_objects", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Student = _module.Student
BankAccount = _module.BankAccount


# ---------------------------------------------------------------------------
# Student tests
# ---------------------------------------------------------------------------

def test_student_stores_name_and_marks():
    student = Student("Ada", 85)
    assert student.name == "Ada"
    assert student.marks == 85


def test_display_details_prints_name_and_marks():
    student = Student("Ben", 35)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        student.display_details()
    output = buffer.getvalue()
    assert "Ben" in output
    assert "35" in output


def test_is_passed_true_for_marks_at_least_40():
    assert Student("Ada", 40).is_passed() is True   # boundary: exactly 40
    assert Student("Ben", 75).is_passed() is True
    assert Student("Cid", 100).is_passed() is True


def test_is_passed_false_for_marks_below_40():
    assert Student("Ada", 39).is_passed() is False
    assert Student("Ben", 0).is_passed() is False
    assert Student("Cid", 30).is_passed() is False


def test_student_marks_can_be_float():
    student = Student("Ada", 40.5)
    assert student.is_passed() is True


def test_different_students_are_independent():
    student1 = Student("Ada", 85)
    student2 = Student("Ben", 35)
    assert student1.name != student2.name
    assert student1.marks != student2.marks
    assert student1.is_passed() is True
    assert student2.is_passed() is False


def test_student_invalid_name_raises_value_error():
    for invalid_name in ["", "   ", None, 123]:
        try:
            Student(invalid_name, 50)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Student({invalid_name!r}, 50) did not raise ValueError")


def test_student_invalid_marks_raises_value_error():
    for invalid_marks in [-1, 101, "85", True]:
        try:
            Student("Ada", invalid_marks)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Student('Ada', {invalid_marks!r}) did not raise ValueError")


# ---------------------------------------------------------------------------
# BankAccount tests
# ---------------------------------------------------------------------------

def test_bank_account_stores_owner_and_balance():
    account = BankAccount("Ada", 100)
    assert account.owner == "Ada"
    assert account.balance == 100


def test_get_balance_returns_current_balance():
    account = BankAccount("Ben", 50)
    assert account.get_balance() == 50


def test_deposit_positive_amount_increases_balance():
    account = BankAccount("Ada", 100)
    account.deposit(25)
    assert account.get_balance() == 125


def test_multiple_deposits_accumulate():
    account = BankAccount("Ada", 0)
    account.deposit(10)
    account.deposit(20)
    account.deposit(5)
    assert account.get_balance() == 35


def test_successful_withdrawal_reduces_balance():
    account = BankAccount("Ada", 100)
    account.withdraw(40)
    assert account.get_balance() == 60


def test_withdrawal_entire_balance_leaves_zero():
    account = BankAccount("Ada", 50)
    account.withdraw(50)
    assert account.get_balance() == 0


def test_insufficient_balance_raises_and_balance_unchanged():
    account = BankAccount("Ada", 50)
    try:
        account.withdraw(100)
    except ValueError:
        pass
    else:
        raise AssertionError("Withdrawal of 100 from balance 50 did not raise ValueError")
    assert account.get_balance() == 50  # unchanged after rejection


def test_deposit_invalid_amounts_raise_value_error():
    account = BankAccount("Ada", 100)
    for invalid_amount in [0, -10, "50", None, True]:
        before = account.get_balance()
        try:
            account.deposit(invalid_amount)
        except ValueError:
            assert account.get_balance() == before  # unchanged
        else:
            raise AssertionError(f"deposit({invalid_amount!r}) did not raise ValueError")


def test_withdraw_invalid_amounts_raise_value_error():
    account = BankAccount("Ada", 100)
    for invalid_amount in [0, -10, "50", None, True]:
        before = account.get_balance()
        try:
            account.withdraw(invalid_amount)
        except ValueError:
            assert account.get_balance() == before  # unchanged
        else:
            raise AssertionError(f"withdraw({invalid_amount!r}) did not raise ValueError")


def test_withdrawal_exceeding_balance_does_not_change_balance():
    account = BankAccount("Ada", 30)
    before = account.get_balance()
    try:
        account.withdraw(31)
    except ValueError:
        pass
    else:
        raise AssertionError("withdraw(31) from balance 30 did not raise ValueError")
    assert account.get_balance() == before


def test_negative_initial_balance_raises_value_error():
    try:
        BankAccount("Ada", -5)
    except ValueError:
        pass
    else:
        raise AssertionError("BankAccount('Ada', -5) did not raise ValueError")


def test_invalid_owner_raises_value_error():
    for invalid_owner in ["", "   ", None, 123]:
        try:
            BankAccount(invalid_owner, 100)
        except ValueError:
            pass
        else:
            raise AssertionError(f"BankAccount({invalid_owner!r}, 100) did not raise ValueError")


def test_two_accounts_are_independent():
    account1 = BankAccount("Ada", 100)
    account2 = BankAccount("Ben", 50)
    account1.deposit(500)
    assert account2.get_balance() == 50  # account2 unaffected
    account2.withdraw(10)
    assert account1.get_balance() == 600  # account1 unaffected


if __name__ == "__main__":
    test_student_stores_name_and_marks()
    test_display_details_prints_name_and_marks()
    test_is_passed_true_for_marks_at_least_40()
    test_is_passed_false_for_marks_below_40()
    test_student_marks_can_be_float()
    test_different_students_are_independent()
    test_student_invalid_name_raises_value_error()
    test_student_invalid_marks_raises_value_error()

    test_bank_account_stores_owner_and_balance()
    test_get_balance_returns_current_balance()
    test_deposit_positive_amount_increases_balance()
    test_multiple_deposits_accumulate()
    test_successful_withdrawal_reduces_balance()
    test_withdrawal_entire_balance_leaves_zero()
    test_insufficient_balance_raises_and_balance_unchanged()
    test_deposit_invalid_amounts_raise_value_error()
    test_withdraw_invalid_amounts_raise_value_error()
    test_withdrawal_exceeding_balance_does_not_change_balance()
    test_negative_initial_balance_raises_value_error()
    test_invalid_owner_raises_value_error()
    test_two_accounts_are_independent()

    print("All test_day15_oop_classes_and_objects tests passed!")