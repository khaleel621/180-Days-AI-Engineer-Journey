"""
Tests for Day 23 - Binary Trees: Introduction and Traversals in
02-data-structures-algorithms/trees/day23-binary-tree-traversals.py.

Covers:
    - BinaryTreeNode creation (value, left, right).
    - Inorder traversal (Left, Root, Right).
    - Preorder traversal (Root, Left, Right).
    - Postorder traversal (Left, Right, Root).
    - Edge cases: empty tree (None), single-node tree, larger tree.
    - Height and depth of a tree.

The implementation is loaded by file path so the tests work regardless of
the current working directory.
"""

import importlib.util
import os

# Load day23-binary-tree-traversals.py by file path.
_module_path = os.path.join(os.path.dirname(__file__),
                            "day23-binary-tree-traversals.py")
_spec = importlib.util.spec_from_file_location(
    "day23_binary_tree_traversals", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

BinaryTreeNode = _module.BinaryTreeNode
inorder_traversal = _module.inorder_traversal
preorder_traversal = _module.preorder_traversal
postorder_traversal = _module.postorder_traversal
tree_height = _module.tree_height
node_depth = _module.node_depth
build_example_tree = _module.build_example_tree
build_single_node_tree = _module.build_single_node_tree


def _build_larger_tree():
    r"""Build a larger tree (7 nodes) and return its root.

            1
           / \
          2   3
         / \   \
        4   5   6
             \
              7

    Expected traversals:
        Inorder:    [4, 2, 5, 7, 1, 3, 6]
        Preorder:   [1, 2, 4, 5, 7, 3, 6]
        Postorder:  [4, 7, 5, 2, 6, 3, 1]
    """
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.left.right.right = BinaryTreeNode(7)
    root.right.right = BinaryTreeNode(6)
    return root


# -----------------------------------------------------------
# Example tree traversals (5 nodes)
# -----------------------------------------------------------

def test_inorder_traversal_example_tree():
    """Inorder of the example tree is [4, 2, 5, 1, 3]."""
    root = build_example_tree()
    assert inorder_traversal(root) == [4, 2, 5, 1, 3]


def test_preorder_traversal_example_tree():
    """Preorder of the example tree is [1, 2, 4, 5, 3]."""
    root = build_example_tree()
    assert preorder_traversal(root) == [1, 2, 4, 5, 3]


def test_postorder_traversal_example_tree():
    """Postorder of the example tree is [4, 5, 2, 3, 1]."""
    root = build_example_tree()
    assert postorder_traversal(root) == [4, 5, 2, 3, 1]


# -----------------------------------------------------------
# Edge case: empty tree (None)
# -----------------------------------------------------------

def test_inorder_empty_tree_returns_empty_list():
    assert inorder_traversal(None) == []


def test_preorder_empty_tree_returns_empty_list():
    assert preorder_traversal(None) == []


def test_postorder_empty_tree_returns_empty_list():
    assert postorder_traversal(None) == []


# -----------------------------------------------------------
# Edge case: single-node tree
# -----------------------------------------------------------

def test_single_node_tree_traversals():
    """A single-node tree returns [value] for all three traversals."""
    single = build_single_node_tree(7)
    assert inorder_traversal(single) == [7]
    assert preorder_traversal(single) == [7]
    assert postorder_traversal(single) == [7]


# -----------------------------------------------------------
# Larger tree (7 nodes)
# -----------------------------------------------------------

def test_larger_tree_traversals():
    root = _build_larger_tree()
    assert inorder_traversal(root) == [4, 2, 5, 7, 1, 3, 6]
    assert preorder_traversal(root) == [1, 2, 4, 5, 7, 3, 6]
    assert postorder_traversal(root) == [4, 7, 5, 2, 6, 3, 1]
# -----------------------------------------------------------
# Height and depth
# -----------------------------------------------------------

def test_tree_height_example_tree():
    """Height of the example tree is 2."""
    root = build_example_tree()
    assert tree_height(root) == 2


def test_tree_height_empty_tree_is_minus_one():
    assert tree_height(None) == -1


def test_tree_height_single_node_is_zero():
    single = build_single_node_tree(7)
    assert tree_height(single) == 0


def test_tree_height_larger_tree():
    """Larger tree height: longest path 1->2->5->7 has 3 edges."""
    root = _build_larger_tree()
    assert tree_height(root) == 3


def test_node_depth_example_tree():
    root = build_example_tree()
    assert node_depth(root, 1) == 0      # root
    assert node_depth(root, 2) == 1      # left child of root
    assert node_depth(root, 3) == 1      # right child of root
    assert node_depth(root, 4) == 2      # leaf
    assert node_depth(root, 5) == 2      # leaf


def test_node_depth_not_found_returns_minus_one():
    root = build_example_tree()
    assert node_depth(root, 99) == -1


def test_node_depth_empty_tree_returns_minus_one():
    assert node_depth(None, 1) == -1


if __name__ == "__main__":
    test_inorder_traversal_example_tree()
    test_preorder_traversal_example_tree()
    test_postorder_traversal_example_tree()
    test_inorder_empty_tree_returns_empty_list()
    test_preorder_empty_tree_returns_empty_list()
    test_postorder_empty_tree_returns_empty_list()
    test_single_node_tree_traversals()
    test_larger_tree_traversals()
    test_tree_height_example_tree()
    test_tree_height_empty_tree_is_minus_one()
    test_tree_height_single_node_is_zero()
    test_tree_height_larger_tree()
    test_node_depth_example_tree()
    test_node_depth_not_found_returns_minus_one()
    test_node_depth_empty_tree_returns_minus_one()
    print("All test_day23_binary_tree_traversals tests passed!")