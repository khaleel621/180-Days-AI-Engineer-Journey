"""
Tests for Day 11 — is_anagram() in
02-data-structures-algorithms/strings/is_anagram.py.

Covers: valid anagrams, invalid anagrams, different string lengths,
empty strings, single-character strings, repeated characters, case sensitivity.
"""

import importlib.util
import os

# Load is_anagram.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "is_anagram.py")
_spec = importlib.util.spec_from_file_location("is_anagram", _module_path)
_anagram_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_anagram_module)

is_anagram = _anagram_module.is_anagram


# ------------------------------------------------------------
# Valid anagram tests
# ------------------------------------------------------------

def test_valid_anagram_listen_silent():
    """'listen' and 'silent' are anagrams."""
    assert is_anagram("listen", "silent") is True


def test_valid_anagram_anagram_nagaram():
    """'anagram' and 'nagaram' are anagrams."""
    assert is_anagram("anagram", "nagaram") is True


def test_valid_anagram_single_char():
    """Same single character strings are anagrams."""
    assert is_anagram("a", "a") is True


def test_valid_anagram_empty_strings():
    """Two empty strings are anagrams."""
    assert is_anagram("", "") is True


# ------------------------------------------------------------
# Invalid anagram tests
# ------------------------------------------------------------

def test_invalid_anagram_hello_world():
    """'hello' and 'world' are not anagrams."""
    assert is_anagram("hello", "world") is False


def test_invalid_anagram_rat_car():
    """'rat' and 'car' are not anagrams."""
    assert is_anagram("rat", "car") is False


def test_invalid_anagram_a_ab():
    """'a' and 'ab' are not anagrams (different lengths)."""
    assert is_anagram("a", "ab") is False


# ------------------------------------------------------------
# Different string lengths
# ------------------------------------------------------------

def test_different_lengths_ab_abc():
    """Strings of different lengths cannot be anagrams."""
    assert is_anagram("ab", "abc") is False


def test_different_lengths_empty_nonempty():
    """Empty vs non-empty strings are not anagrams."""
    assert is_anagram("", "a") is False


# ------------------------------------------------------------
# Empty strings
# ------------------------------------------------------------

def test_both_empty_strings():
    """Two empty strings are anagrams."""
    assert is_anagram("", "") is True


# ------------------------------------------------------------
# Single-character strings
# ------------------------------------------------------------

def test_single_char_same():
    """Same single character is an anagram."""
    assert is_anagram("x", "x") is True


def test_single_char_different():
    """Different single characters are not anagrams."""
    assert is_anagram("a", "b") is False


# ------------------------------------------------------------
# Repeated characters
# ------------------------------------------------------------

def test_repeated_characters_aabb_bbaa():
    """Strings with repeated characters in different order."""
    assert is_anagram("aabb", "bbaa") is True


def test_repeated_characters_different_counts():
    """Same characters but different frequencies."""
    assert is_anagram("aab", "abb") is False


# ------------------------------------------------------------
# Case sensitivity
# ------------------------------------------------------------

def test_case_sensitive_Aa_aA():
    """Uppercase and lowercase are different characters."""
    assert is_anagram("Aa", "aA") is True


def test_case_sensitive_Aa_aa():
    """Mixed case vs same case are not anagrams."""
    assert is_anagram("Aa", "aa") is False


if __name__ == "__main__":
    test_valid_anagram_listen_silent()
    test_valid_anagram_anagram_nagaram()
    test_valid_anagram_single_char()
    test_valid_anagram_empty_strings()

    test_invalid_anagram_hello_world()
    test_invalid_anagram_rat_car()
    test_invalid_anagram_a_ab()

    test_different_lengths_ab_abc()
    test_different_lengths_empty_nonempty()

    test_both_empty_strings()

    test_single_char_same()
    test_single_char_different()

    test_repeated_characters_aabb_bbaa()
    test_repeated_characters_different_counts()

    test_case_sensitive_Aa_aA()
    test_case_sensitive_Aa_aa()

    print("All day11-valid-anagram tests passed!")