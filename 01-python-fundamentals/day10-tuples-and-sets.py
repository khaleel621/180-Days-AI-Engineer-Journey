"""
Day 10 — Python Fundamentals: Tuples and Sets

Topic: Tuples and Sets

This file teaches beginner-friendly tuple and set concepts with examples,
plus two practice exercises:
  1. tuple_information(items)
  2. remove_duplicates(numbers)

Learner practice is pending — completing the exercises yourself is required
to mark this day complete.
"""

# ============================================================================
# 1. WHAT IS A TUPLE?
# ============================================================================
# A tuple is an ordered, immutable collection of items.
# "Ordered" means items have a fixed position (index).
# "Immutable" means once created, you cannot add, remove, or change items.
# Tuples are written with parentheses ().

# ============================================================================
# 2. CREATING TUPLES
# ============================================================================

# Empty tuple
empty_tuple = ()

# Tuple with items
fruits = ("apple", "banana", "cherry")

# Tuple with mixed types
mixed = (1, "hello", 3.14, True)

# Single-element tuple needs a trailing comma (otherwise it's just a value in parens)
single = (42,)          # this is a tuple
not_a_tuple = (42)      # this is just the integer 42

# Tuple without parentheses (tuple packing)
packed = 1, 2, 3        # same as (1, 2, 3)

# ============================================================================
# 3. ACCESSING TUPLE ELEMENTS
# ============================================================================

# Use square brackets with an index, starting at 0
print(fruits[0])        # "apple"
print(fruits[1])        # "banana"
print(fruits[2])        # "cherry"

# Negative indexing counts from the end
print(fruits[-1])       # "cherry"
print(fruits[-2])       # "banana"

# ============================================================================
# 4. TUPLE INDEXING
# ============================================================================

# Index        0       1       2
#              |       |       |
# fruits = ("apple", "banana", "cherry")
# Negative     -3      -2      -1

# Access by positive index:
first = fruits[0]       # "apple"

# Access by negative index:
last = fruits[-1]       # "cherry"

# ============================================================================
# 5. WHY TUPLES ARE IMMUTABLE
# ============================================================================

# Once created, you cannot change, add, or remove items:
# fruits[0] = "orange"   # TypeError: 'tuple' object does not support item assignment
# fruits.append("date")  # AttributeError: 'tuple' object has no attribute 'append'
# del fruits[1]          # TypeError: 'tuple' object doesn't support item deletion

# Immutability is useful when you want to guarantee data won't change
# (for example, coordinates, RGB colors, or database records).

# ============================================================================
# 6. WHAT IS A SET?
# ============================================================================
# A set is an unordered collection of unique items.
# "Unordered" means items have no fixed position — no indexing.
# "Unique" means duplicates are automatically removed.
# Sets are written with curly braces {}.

# ============================================================================
# 7. CREATING SETS
# ============================================================================

# Empty set (must use set(), not {} — {} creates an empty dictionary)
empty_set = set()

# Set with items
numbers = {1, 2, 3, 4, 5}

# Set with duplicates — duplicates are removed automatically
with_dupes = {1, 2, 2, 3, 3, 3}   # becomes {1, 2, 3}

# Set from a list
from_list = set([1, 2, 2, 3])     # becomes {1, 2, 3}

# ============================================================================
# 8. REMOVING DUPLICATE VALUES USING SETS
# ============================================================================

original = [1, 2, 2, 3, 4, 4, 5]
unique = set(original)            # {1, 2, 3, 4, 5}
# Note: sets do NOT guarantee the original ordering.

# ============================================================================
# 9. ADDING AND REMOVING SET ELEMENTS
# ============================================================================

my_set = {1, 2, 3}

# Add an element
my_set.add(4)                     # {1, 2, 3, 4}

# Add multiple elements
my_set.update([5, 6])             # {1, 2, 3, 4, 5, 6}

# Remove an element (raises KeyError if not present)
my_set.remove(6)                  # {1, 2, 3, 4, 5}

# Discard an element (no error if not present)
my_set.discard(100)               # no error, set unchanged

# Remove and return an arbitrary element
popped = my_set.pop()             # removes some element, returns it

# Clear all elements
# my_set.clear()                  # empties the set

# ============================================================================
# 10. BASIC SET OPERATIONS
# ============================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union — all elements from both sets
union_result = set_a | set_b          # {1, 2, 3, 4, 5, 6}
# or: set_a.union(set_b)

# Intersection — elements in both sets
intersection_result = set_a & set_b   # {3, 4}
# or: set_a.intersection(set_b)

# Difference — elements in set_a but not in set_b
difference_result = set_a - set_b     # {1, 2}
# or: set_a.difference(set_b)

# Symmetric difference — elements in either set but not both
sym_diff_result = set_a ^ set_b       # {1, 2, 5, 6}
# or: set_a.symmetric_difference(set_b)

# Subset / Superset
print({1, 2} <= set_a)       # True — {1, 2} is a subset of set_a

# ============================================================================
# EXERCISE 1 — TUPLE INFORMATION
# ============================================================================

def tuple_information(items):
    """
    Return useful information about a tuple.

    Args:
        items: A tuple of any elements.

    Returns:
        A dictionary with:
            - "count": number of elements in the tuple
            - "first": the first element (None if empty)
            - "last": the last element (None if empty)

    Example:
        tuple_information((10, 20, 30))
        -> {"count": 3, "first": 10, "last": 30}

        tuple_information(())
        -> {"count": 0, "first": None, "last": None}
    """
    if len(items) == 0:
        return {"count": 0, "first": None, "last": None}

    return {
        "count": len(items),
        "first": items[0],
        "last": items[-1],
    }


# ============================================================================
# EXERCISE 2 — REMOVE DUPLICATES
# ============================================================================

def remove_duplicates(numbers):
    """
    Return a collection of unique values from the input list.

    Uses a set to identify unique values. Sets do NOT guarantee the
    original ordering of elements.

    The original input list is NOT modified.

    Args:
        numbers: A list of numbers (may contain duplicates).

    Returns:
        A list of unique values from the input (order not guaranteed).

    Example:
        remove_duplicates([1, 2, 2, 3, 1])
        -> [1, 2, 3]  (order may vary)
    """
    # Convert to a set to remove duplicates, then back to a list.
    # The original list is not modified because we create a new set.
    return list(set(numbers))


def main():
    print("=" * 60)
    print("Day 10 — Python Fundamentals: Tuples and Sets")
    print("=" * 60)
    print()

    # --- Tuple examples ---
    print("--- Tuples ---")
    print(f"empty_tuple: {empty_tuple}")
    print(f"fruits: {fruits}")
    print(f"mixed: {mixed}")
    print(f"single: {single}")
    print(f"not_a_tuple: {not_a_tuple} (type: {type(not_a_tuple).__name__})")
    print(f"packed: {packed}")
    print()

    print("Accessing elements:")
    print(f"  fruits[0] = {fruits[0]}")
    print(f"  fruits[-1] = {fruits[-1]}")
    print()

    print("Tuple indexing:")
    print("  Index:    0       1       2")
    print("  Value:   'apple' 'banana' 'cherry'")
    print("  Negative: -3      -2      -1")
    print()

    print("Immutability: tuples cannot be changed after creation.")
    print("  fruits[0] = 'orange'  -> TypeError")
    print("  fruits.append('date')   -> AttributeError")
    print()

    # --- Set examples ---
    print("--- Sets ---")
    print(f"empty_set: {empty_set}")
    print(f"numbers: {numbers}")
    print(f"with_dupes: {with_dupes}  (duplicates removed)")
    print(f"from_list: {from_list}")
    print()

    print("Removing duplicates:")
    print(f"  original: {original}")
    print(f"  unique:   {unique}")
    print("  Note: sets do NOT guarantee original ordering.")
    print()

    print("Adding and removing elements:")
    demo_set = {1, 2, 3}
    print(f"  start: {demo_set}")
    demo_set.add(4)
    print(f"  after add(4): {demo_set}")
    demo_set.remove(2)
    print(f"  after remove(2): {demo_set}")
    print()

    print("Basic set operations:")
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(f"  set_a = {set_a}")
    print(f"  set_b = {set_b}")
    print(f"  union:      {set_a | set_b}")
    print(f"  intersection: {set_a & set_b}")
    print(f"  difference:   {set_a - set_b}")
    print(f"  sym_diff:     {set_a ^ set_b}")
    print()

    # --- Exercise 1 demo ---
    print("--- Exercise 1: tuple_information ---")
    print(f"  tuple_information((10, 20, 30)) = {tuple_information((10, 20, 30))}")
    print(f"  tuple_information(()) = {tuple_information(())}")
    print()

    # --- Exercise 2 demo ---
    print("--- Exercise 2: remove_duplicates ---")
    print(f"  remove_duplicates([1, 2, 2, 3, 1]) = {remove_duplicates([1, 2, 2, 3, 1])}")
    print("  Original list unchanged: [1, 2, 2, 3, 1]")
    print()

    print("=" * 60)
    print("Learner practice: complete the exercises yourself to mark Day 10 complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
print(set_a >= {1, 2})       # True — set_a is a superset of {1, 2}