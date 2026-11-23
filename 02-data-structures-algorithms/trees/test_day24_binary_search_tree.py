"""
Tests for Day 24 - Binary Search Trees: Search and Insertion in
02-data-structures-algorithms/trees/day24-binary-search-tree.py.

Covers:
    - BSTNode creation (value, left, right).
    - Inserting multiple values into a BST.
    - Searching for existing values (returns the node).
    - Searching for missing values (returns None).
    - Inserting into an empty BST (root starts as None).
    - Duplicate values: documented rule — duplicates go to the LEFT subtree,
      so both copies appear in inorder output and the output stays sorted.
    - Inorder traversal gives values in non-decreasing (sorted) order.
    - Edge cases: empty tree, single-node tree.

The implementation is loaded by file path so the tests work regardless of
the current working directory.
"""

import importlib.util
import os

# Load day24-binary-search-tree.py by file path.
_module_path = os.path.join(os.path.dirname(__file__),
                            "day24-binary-search-tree.py")
_spec = importlib.util.spec_from_file_location(
    "day24_binary_search_tree", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

BSTNode = _module.BSTNode
insert = _module.insert
search = _module.search
inorder_traversal = _module.inorder_traversal
build_example_bst = _module.build_example_bst
build_single_node_tree = _module.build_single_node_tree


def _build_bst(values):
    """Insert every value into an initially empty BST and return its root."""
    root = None
    for value in values:
        root = insert(root, value)
    return root


# -----------------------------------------------------------
# Inserting multiple values
# -----------------------------------------------------------

def test_insert_multiple_values_inorder_is_sorted():
    """Inserting [50, 30, 70, 20, 40, 60, 80] then inorder gives sorted order."""
    root = _build_bst([50, 30, 70, 20, 40, 60, 80])
    assert inorder_traversal(root) == [20, 30, 40, 50, 60, 70, 80]


def test_insert_unsorted_input_still_sorted_inorder():
    """Whatever the insert order, inorder of a BST is sorted."""
    root = _build_bst([5, 3, 8, 1, 4, 7, 9])
    assert inorder_traversal(root) == [1, 3, 4, 5, 7, 8, 9]


def test_insert_returns_root_for_chaining():
    """insert() returns the root, so callers keep a reference to the tree."""
    root = None
    root = insert(root, 10)
    root = insert(root, 5)
    root = insert(root, 15)
    assert root.value == 10
    assert root.left.value == 5
    assert root.right.value == 15


# -----------------------------------------------------------
# Searching for existing values
# -----------------------------------------------------------

def test_search_existing_value_returns_node():
    """search() returns the BSTNode holding the value."""
    root = build_example_bst()
    assert search(root, 50).value == 50   # root
    assert search(root, 30).value == 30   # left child
    assert search(root, 70).value == 70   # right child
    assert search(root, 20).value == 20   # leaf
    assert search(root, 80).value == 80   # leaf


def test_search_found_is_not_none():
    """A found search result can be checked with `is not None`."""
    root = build_example_bst()
    assert search(root, 40) is not None


# -----------------------------------------------------------
# Searching for missing values
# -----------------------------------------------------------

def test_search_missing_value_returns_none():
    """search() returns None for a value not in the tree."""
    root = build_example_bst()
    assert search(root, 100) is None
    assert search(root, 45) is None
    assert search(root, 10) is None


# -----------------------------------------------------------
# Inserting into an empty BST
# -----------------------------------------------------------

def test_insert_into_empty_bst_creates_single_node():
    """insert(None, value) returns a new single-node tree."""
    root = None
    root = insert(root, 42)
    assert isinstance(root, BSTNode)
    assert root.value == 42
    assert root.left is None
    assert root.right is None
    assert inorder_traversal(root) == [42]


def test_single_node_tree():
    """A single-node BST finds its own value and nothing else."""
    root = build_single_node_tree(7)
    assert search(root, 7).value == 7
    assert search(root, 8) is None
    assert search(root, 6) is None
    assert inorder_traversal(root) == [7]


# -----------------------------------------------------------
# Duplicate values (documented rule: duplicates go to the LEFT subtree)
# -----------------------------------------------------------

def test_duplicate_values_appear_in_inorder():
    """Inserting 30 twice keeps both copies and output stays sorted."""
    root = build_example_bst()
    root = insert(root, 30)   # duplicate of the existing 30
    assert inorder_traversal(root) == [20, 30, 30, 40, 50, 60, 70, 80]


def test_duplicate_goes_to_left_subtree():
    """The documented duplicate rule: equal values go into the left subtree."""
    root = build_example_bst()   # root.left holds 30; its right holds 40
    original_30 = root.left
    root = insert(root, 30)
    # The duplicate 30 must appear in the original 30 node's LEFT subtree,
    # not in its RIGHT subtree (which holds strictly greater values).
    assert 30 in inorder_traversal(original_30.left)
    assert 30 not in inorder_traversal(original_30.right)
    # Searching for 30 still finds a node with value 30.
    assert search(root, 30).value == 30


# -----------------------------------------------------------
# Inorder traversal edge cases
# -----------------------------------------------------------

def test_inorder_empty_tree_returns_empty_list():
    assert inorder_traversal(None) == []


def test_inorder_single_node():
    single = build_single_node_tree(99)
    assert inorder_traversal(single) == [99]


def test_search_empty_tree_returns_none():
    assert search(None, 1) is None


if __name__ == "__main__":
    test_insert_multiple_values_inorder_is_sorted()
    test_insert_unsorted_input_still_sorted_inorder()
    test_insert_returns_root_for_chaining()
    test_search_existing_value_returns_node()
    test_search_found_is_not_none()
    test_search_missing_value_returns_none()
    test_insert_into_empty_bst_creates_single_node()
    test_single_node_tree()
    test_duplicate_values_appear_in_inorder()
    test_duplicate_goes_to_left_subtree()
    test_inorder_empty_tree_returns_empty_list()
    test_inorder_single_node()
    test_search_empty_tree_returns_none()
    print("All test_day24_binary_search_tree tests passed!")


