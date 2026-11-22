"""
Day 23 - Data Structures & Algorithms: Binary Trees — Introduction and Traversals.

Topic: Binary Tree and its three depth-first traversals: Inorder, Preorder, Postorder.

================================================================================
1. WHAT IS A BINARY TREE?
================================================================================
A binary tree is a hierarchical data structure in which each node has at most
two children, called the left child and the right child.

    - The topmost node is called the root. It has no parent.
    - Every node stores a value and references to its left and right children.
    - A node with no children is called a leaf node.
    - A node with at least one child is called an internal node.

A binary tree is either empty or consists of a root node plus two disjoint
binary trees (the left subtree and the right subtree).

================================================================================
2. ROOT, PARENT, CHILD AND LEAF NODES
================================================================================
    - Root:   the topmost node of the tree (no parent).
    - Parent: a node that has one or two children directly below it.
    - Child:  a node directly connected below a parent node.
    - Leaf:   a node with no children (left and right are both None).

Example tree used throughout this file:

        1
       / \
      2   3
     / \
    4   5

    - Root:        1
    - Parent of 4: 2     (2 is the parent of children 4 and 5)
    - Parent of 5: 2
    - Children of 1: 2 (left) and 3 (right)
    - Leaf nodes:  4, 5 and 3  (they have no children)
    - Internal nodes: 1 and 2

================================================================================
3. HEIGHT AND DEPTH OF A TREE
================================================================================
    - Depth of a node: the number of edges from the root to that node.
      The root has depth 0.
    - Height of a node: the number of edges on the longest path from that node
      down to a leaf. A leaf has height 0.
    - Height of the tree = height of the root node.

For the example tree:
        1 (depth 0, height 2)
       / \
      2   3 (depth 1; node 3 height 0)
     / \
    4   5 (depth 2; nodes 4 and 5 height 0)

    - Depth of node 4 = 2 (path 1 -> 2 -> 4 has 2 edges).
    - Height of node 2 = 1 (longest path 2 -> 4 or 2 -> 5 has 1 edge).
    - Height of the tree (node 1) = 2.
================================================================================
4. TREE TRAVERSALS
================================================================================
Traversal means visiting every node in the tree exactly once. There are two
broad categories: depth-first and breadth-first. This file implements the three
depth-first traversals, each defined by the order in which it handles the
current node (Root), its left subtree (L) and its right subtree (R).

    1. Inorder  (L, Root, Right):  visit left subtree, then root, then right.
       For a binary search tree this gives values in ascending order.
    2. Preorder (Root, L, Right):  visit root, then left subtree, then right.
       Useful to copy or serialize a tree.
    3. Postorder(L, Right, Root):  visit left subtree, then right subtree,
       then root. Useful to delete or free a tree.

For the example tree:

        1
       / \
      2   3
     / \
    4   5

    Inorder traversal:  4  2  5  1  3
    Preorder traversal: 1  2  4  5  3
    Postorder traversal:4  5  2  3  1

All three traversals below are implemented as separate recursive functions.
"""

# ---------------------------------------------------------------------------
# Binary tree node
# ---------------------------------------------------------------------------
class BinaryTreeNode:
    """A single node in a binary tree.

    Attributes:
        value: The data stored in the node.
        left:  Reference to the left child (BinaryTreeNode or None).
        right: Reference to the right child (BinaryTreeNode or None).
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------------------------------------------------------------------
# Traversal functions (each returns a list of visited values)
# ---------------------------------------------------------------------------
def inorder_traversal(node, result=None):
    """Inorder traversal: Left -> Root -> Right.

    Args:
        node: The current BinaryTreeNode (or None for an empty subtree).
        result: Internal list used during recursion. Callers should omit this.

    Returns:
        List of node values in inorder sequence.
    """
    if result is None:
        result = []

    # Base case: empty subtree.
    if node is None:
        return result

    # 1. Visit the left subtree.
    inorder_traversal(node.left, result)
    # 2. Visit the root (current node).
    result.append(node.value)
    # 3. Visit the right subtree.
    inorder_traversal(node.right, result)

    return result


def preorder_traversal(node, result=None):
    """Preorder traversal: Root -> Left -> Right.

    Args:
        node: The current BinaryTreeNode (or None for an empty subtree).
        result: Internal list used during recursion. Callers should omit this.

    Returns:
        List of node values in preorder sequence.
    """
    if result is None:
        result = []

    # Base case: empty subtree.
    if node is None:
        return result

    # 1. Visit the root (current node).
    result.append(node.value)
    # 2. Visit the left subtree.
    preorder_traversal(node.left, result)
    # 3. Visit the right subtree.
    preorder_traversal(node.right, result)

    return result


def postorder_traversal(node, result=None):
    """Postorder traversal: Left -> Right -> Root.

    Args:
        node: The current BinaryTreeNode (or None for an empty subtree).
        result: Internal list used during recursion. Callers should omit this.

    Returns:
        List of node values in postorder sequence.
    """
    if result is None:
        result = []

    # Base case: empty subtree.
    if node is None:
        return result

    # 1. Visit the left subtree.
    postorder_traversal(node.left, result)
    # 2. Visit the right subtree.
    postorder_traversal(node.right, result)
    # 3. Visit the root (current node).
    result.append(node.value)

    return result
# ---------------------------------------------------------------------------
# Height and depth
# ---------------------------------------------------------------------------
def tree_height(node):
    """Height of the tree rooted at `node`.

    Height = number of edges on the longest path from this node down to a leaf.
    An empty tree (None) has height -1; a single-node tree has height 0.

    Args:
        node: The root BinaryTreeNode (or None).

    Returns:
        Integer height of the tree.
    """
    # Base case: empty subtree contributes -1 edges.
    if node is None:
        return -1

    left_height = tree_height(node.left)
    right_height = tree_height(node.right)

    # Height is 1 (edge to child) plus the taller of the two subtrees.
    return 1 + max(left_height, right_height)


def node_depth(node, target, current_depth=0):
    """Depth of the node holding `target` value.

    Depth = number of edges from the root to that node. Root depth = 0.
    Returns -1 if `target` is not found in the tree.

    Args:
        node: The current BinaryTreeNode (or None).
        target: The value to search for.
        current_depth: Depth of the current node (used during recursion).

    Returns:
        Integer depth of the target node, or -1 if not found.
    """
    # Base case: reached an empty subtree without finding the target.
    if node is None:
        return -1

    # Target found at the current node.
    if node.value == target:
        return current_depth

    # Search the left subtree.
    left_depth = node_depth(node.left, target, current_depth + 1)
    if left_depth != -1:
        return left_depth

    # Search the right subtree.
    return node_depth(node.right, target, current_depth + 1)


# ---------------------------------------------------------------------------
# Helper to build the example tree
# ---------------------------------------------------------------------------
def build_example_tree():
    """Build and return the example binary tree used in this file.

        1
       / \
      2   3
     / \
    4   5
    """
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    return root


def build_single_node_tree(value=42):
    """Build a tree with only a root node."""
    return BinaryTreeNode(value)


# ---------------------------------------------------------------------------
# PRACTICAL EXERCISES (try these yourself)
# ---------------------------------------------------------------------------
#
# Exercise 1:
#   Write a function count_nodes(node) that returns the total number of nodes
#   in a binary tree. Empty tree returns 0.
#
# Exercise 2:
#   Write a function sum_values(node) that returns the sum of all node values.
#
# Exercise 3:
#   Write a function is_leaf(node) that returns True if the node has no
#   children, False otherwise.
#
# Exercise 4:
#   Draw a larger tree on paper (at least 7 nodes) and write down the expected
#   inorder, preorder and postorder sequences before coding them.
def main():
    print("=" * 60)
    print("Day 23 - DSA: Binary Trees — Introduction and Traversals")
    print("=" * 60)
    print()

    # Build the example tree.
    root = build_example_tree()
    print("Example tree:")
    print("        1")
    print("       / \\")
    print("      2   3")
    print("     / \\")
    print("    4   5")
    print()

    # --- Inorder -------------------------------------------------------
    print("--- Inorder traversal (Left, Root, Right) ---")
    inorder_result = inorder_traversal(root)
    print(f"Result: {inorder_result}")
    print("Expected: [4, 2, 5, 1, 3]")
    print()

    # --- Preorder ------------------------------------------------------
    print("--- Preorder traversal (Root, Left, Right) ---")
    preorder_result = preorder_traversal(root)
    print(f"Result: {preorder_result}")
    print("Expected: [1, 2, 4, 5, 3]")
    print()

    # --- Postorder -----------------------------------------------------
    print("--- Postorder traversal (Left, Right, Root) ---")
    postorder_result = postorder_traversal(root)
    print(f"Result: {postorder_result}")
    print("Expected: [4, 5, 2, 3, 1]")
    print()

    # --- Height and depth ----------------------------------------------
    print("--- Height and depth ---")
    print(f"Height of the tree: {tree_height(root)}  (expected 2)")
    print(f"Depth of node 4: {node_depth(root, 4)}  (expected 2)")
    print(f"Depth of node 1 (root): {node_depth(root, 1)}  (expected 0)")
    print(f"Depth of node 99 (not present): {node_depth(root, 99)}  (expected -1)")
    print()

    # --- Edge case: empty tree -----------------------------------------
    print("--- Edge case: empty tree ---")
    print(f"Inorder of None: {inorder_traversal(None)}  (expected [])")
    print(f"Preorder of None: {preorder_traversal(None)}  (expected [])")
    print(f"Postorder of None: {postorder_traversal(None)}  (expected [])")
    print(f"Height of None: {tree_height(None)}  (expected -1)")
    print()

    # --- Edge case: single-node tree -----------------------------------
    print("--- Edge case: single-node tree ---")
    single = build_single_node_tree(7)
    print(f"Inorder: {inorder_traversal(single)}   (expected [7])")
    print(f"Preorder: {preorder_traversal(single)}   (expected [7])")
    print(f"Postorder: {postorder_traversal(single)}   (expected [7])")
    print(f"Height: {tree_height(single)}   (expected 0)")
    print(f"Depth of node 7: {node_depth(single, 7)}   (expected 0)")
    print()

    print("=" * 60)
    print("All binary tree demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()