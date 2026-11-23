"""
Day 24 - Data Structures & Algorithms: Binary Search Trees — Search and Insertion

Topic: Binary Search Tree (BST) — ordering property, search, insertion,
inorder traversal, recursion, and time complexity.

This file continues from Day 23 (Binary Trees and their traversals). If you
have not reviewed Day 23 yet, start with
02-data-structures-algorithms/trees/day23-binary-tree-traversals.py.

================================================================================
1. WHAT IS A BINARY SEARCH TREE (BST)?
================================================================================
A binary search tree is a binary tree with an extra rule: the values are kept
in order. Every node stores a value and has at most two children (left and
right).

    - The topmost node is the root.
    - A node with no children is a leaf.
    - For every node, all values in its left subtree are smaller than (or
      equal to, per our duplicate rule below) the node's value, and all
      values in its right subtree are greater than the node's value.

Example BST (built by inserting 50, 30, 70, 20, 40, 60, 80):

        50
       /  \
     30    70
    /  \   /  \
   20  40 60   80

================================================================================
2. BINARY TREE VS BINARY SEARCH TREE
================================================================================
|                        | Binary Tree                  | Binary Search Tree       |
|------------------------|------------------------------|--------------------------|
| Rule for children      | Any order, no rule           | Ordered by value         |
| Left subtree values    | No restriction               | Less than the node       |
| Right subtree values   | No restriction               | Greater than the node    |
| Searching              | May need to visit all nodes  | Can skip half the tree   |
| Example use case       | Hierarchical data (org chart)| Sorted lookup, sets/maps |

A binary search tree IS a binary tree, but a binary tree is NOT necessarily
a binary search tree.

================================================================================
3. BST ORDERING PROPERTY
================================================================================
For every node in the tree:
    - value in left subtree  <= node.value
    - value in right subtree >  node.value

DUPLICATE RULE (documented clearly):
If a value to insert is EQUAL to a node's value, we insert it into the
LEFT subtree of that node. So a node's left subtree holds values <= itself,
and its right subtree holds values strictly greater than itself.

Why this rule? It gives us one consistent place for duplicates, and an
inorder traversal still prints values in non-decreasing (sorted) order.
Other valid choices exist (right subtree, or a count field on the node);
this file picks left subtree and documents it.

================================================================================
4. SEARCHING FOR A VALUE IN A BST
================================================================================
Search uses the ordering property, so we never look at both subtrees:

    - If the current node is None, the value is not in the tree.
    - If the current node's value equals the target, we found it.
    - If the target is smaller, search the LEFT subtree only.
    - If the target is greater, search the RIGHT subtree only.

This is binary search on a tree shape: each step throws away half the
remaining nodes (when the tree is balanced).

================================================================================
5. INSERTING A NEW VALUE INTO A BST
================================================================================
Insertion follows the same path a search would take:

    - If the tree is empty (root is None), the new value becomes the root.
    - If the value <= current node's value, go left; if there is no left
      child, place the new node there.
    - If the value > current node's value, go right; if there is no right
      child, place the new node there.

We return the (possibly new) root from insert() so inserting into an empty
tree works: insert(None, 42) returns a new single-node tree.

================================================================================
6. HOW RECURSION WORKS IN BST OPERATIONS
================================================================================
Both insert() and search() are recursive:

    - Each call handles ONE node, then calls itself on ONE child.
    - The base case is an empty subtree (None): stop and return.
    - insert() rebuilds the path on the way back up:
        root.left = insert(root.left, value)   (or root.right)
      This links the new node into the tree as the recursion unwinds.
    - The call stack depth equals the tree height.

================================================================================
7. TIME COMPLEXITY OF SEARCH AND INSERTION
================================================================================
- Time: O(h) where h is the height of the tree.
  - Balanced tree: h = O(log n) -> fast, like binary search on a sorted list.
  - Skewed tree (every node has one child): h = O(n) -> slow, like a linked list.
- Extra space: O(h) for the recursion call stack.
  - Balanced: O(log n). Worst case (skewed): O(n).

n = number of nodes in the tree.

================================================================================
8. HANDLING EDGE CASES
================================================================================
- Empty tree: search(None, value) returns None; insert(None, value) creates
  a new single-node tree.
- Single-node tree: insert and search work on the root alone.
- Value not present: search returns None.
- Duplicate values: inserted into the left subtree (see documented rule).
- Negative numbers and zero: work like any other value; ordering still applies.
"""

# ---------------------------------------------------------------------------
# BST node (like BinaryTreeNode from Day 23, but with the BST ordering rule)
# ---------------------------------------------------------------------------
class BSTNode:
    """A single node in a Binary Search Tree.

    Attributes:
        value: The data stored in the node.
        left:  Reference to the left child (BSTNode or None). Holds values
               less than or equal to this node's value.
        right: Reference to the right child (BSTNode or None). Holds values
               strictly greater than this node's value.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------------------------------------------------------------------
# Insertion
# ---------------------------------------------------------------------------
def insert(root, value):
    """
    Insert `value` into the BST rooted at `root` and return the root.

    Duplicates go to the left subtree (documented rule:
    left subtree values <= node.value < right subtree values).

    Args:
        root: The root BSTNode of the tree (or None for an empty tree).
        value: The value to insert.

    Returns:
        The root BSTNode of the tree after insertion. When the tree was
        empty, this is the newly created node.
    """
    # Base case: empty tree -> create a new node and return it.
    if root is None:
        return BSTNode(value)

    if value <= root.value:
        # Duplicate or smaller: go left. The documented duplicate rule sends
        # equal values here, so the left subtree may contain duplicates.
        root.left = insert(root.left, value)
    else:
        # Greater: go right.
        root.right = insert(root.right, value)

    # Return the (unchanged) root so the caller's link stays intact.
    # On the way back up the recursion, this re-links each subtree.
    return root


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------
def search(root, value):
    """
    Search for `value` in the BST rooted at `root`.

    Args:
        root: The root BSTNode of the tree (or None for an empty tree).
        value: The value to look for.

    Returns:
        The BSTNode holding `value` if found, otherwise None.
        Callers can check `result is not None` for a yes/no answer.
    """
    # Base case 1: reached an empty subtree -> value not in the tree.
    if root is None:
        return None

    # Base case 2: found the value at the current node.
    if root.value == value:
        return root

    # Recursive step: use the ordering property to skip one subtree.
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


# ---------------------------------------------------------------------------
# Inorder traversal (Left, Root, Right)
# ---------------------------------------------------------------------------
def inorder_traversal(node, result=None):
    """Inorder traversal: Left -> Root -> Right.

    For a BST, this visits values in non-decreasing (sorted) order, which is
    the easiest way to verify the BST ordering property.

    Args:
        node: The current BSTNode (or None for an empty subtree).
        result: Internal list used during recursion. Callers should omit this.

    Returns:
        List of node values in inorder sequence.
    """
    if result is None:
        result = []

    # Base case: empty subtree.
    if node is None:
        return result

    # 1. Visit the left subtree (smaller or equal values).
    inorder_traversal(node.left, result)
    # 2. Visit the root (current node).
    result.append(node.value)
    # 3. Visit the right subtree (greater values).
    inorder_traversal(node.right, result)

    return result


# ---------------------------------------------------------------------------
# Helpers to build and print example trees
# ---------------------------------------------------------------------------
def build_example_bst():
    """Build the example BST by inserting values one by one.

    Insert order: 50, 30, 70, 20, 40, 60, 80

        50
       /  \
     30    70
    /  \   /  \
   20  40 60   80
    """
    root = None
    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, value)
    return root


def build_single_node_tree(value=42):
    """Build a BST with only a root node."""
    return BSTNode(value)


def print_tree(node, indent="", is_left=None):
    """Print a BST in a readable sideways layout (right child on top)."""
    if node is not None:
        print_tree(node.right, indent + "    ", True)
        prefix = ""
        if is_left is True:
            prefix = "/-- "
        elif is_left is False:
            prefix = "\\-- "
        elif is_left is None:
            prefix = ""
        print(f"{indent}{prefix}{node.value}")
        print_tree(node.left, indent + "    ", False)


# ---------------------------------------------------------------------------
# PRACTICAL EXERCISES (try these yourself)
# ---------------------------------------------------------------------------
#
# Exercise 1:
#   Write a function find_min(root) that returns the smallest value in the BST.
#   (Hint: keep going left until there is no left child.)
#
# Exercise 2:
#   Write a function find_max(root) that returns the largest value in the BST.
#   (Hint: keep going right until there is no right child.)
#
# Exercise 3:
#   Without running the code, draw the BST that results from inserting
#   [10, 5, 15, 3, 7, 12, 20] in that order. Then verify by running the code.
#
# Exercise 4:
#   Insert the same value twice (a duplicate) and print the inorder traversal.
#   Confirm the duplicate appears and the output stays sorted.
def main():
    print("=" * 60)
    print("Day 24 - DSA: Binary Search Trees — Search and Insertion")
    print("=" * 60)
    print()

    # --- Build the example BST ------------------------------------------
    print("--- Building a BST by inserting [50, 30, 70, 20, 40, 60, 80] ---")
    root = build_example_bst()
    print("Tree structure (sideways, root in the middle):")
    print_tree(root)
    print()

    # --- Inorder traversal verifies sorted order ------------------------
    print("--- Inorder traversal (Left, Root, Right) ---")
    inorder_result = inorder_traversal(root)
    print(f"Result: {inorder_result}")
    print("Expected: [20, 30, 40, 50, 60, 70, 80] (sorted order)")
    print("(A sorted inorder output confirms the BST ordering property.)")
    print()

    # --- Search: value that exists --------------------------------------
    print("--- Search: value that exists ---")
    found = search(root, 40)
    print(f"search(root, 40) -> {'found node with value 40' if found is not None else 'NOT found'}")
    print("Expected: found node with value 40")
    print()

    # --- Search: value that does not exist ------------------------------
    print("--- Search: value that does not exist ---")
    missing = search(root, 100)
    print(f"search(root, 100) -> {missing}")
    print("Expected: None")
    print()

    # --- Edge case: insert into an empty BST ----------------------------
    print("--- Edge case: inserting into an empty BST ---")
    empty_root = None
    empty_root = insert(empty_root, 42)
    print(f"insert(None, 42) -> root.value = {empty_root.value}")
    print("Expected: root.value = 42 (a new single-node tree)")
    print(f"inorder of empty-root tree: {inorder_traversal(empty_root)}")
    print("Expected: [42]")
    print()

    # --- Edge case: duplicates (documented rule: duplicates go left) ---
    print("--- Edge case: inserting a duplicate value (30 again) ---")
    root_with_duplicate = insert(root, 30)
    inorder_with_dup = inorder_traversal(root_with_duplicate)
    print(f"After insert(root, 30): inorder = {inorder_with_dup}")
    print("Expected: [20, 30, 30, 40, 50, 60, 70, 80]")
    print("The duplicate 30 went to the left subtree of the first 30,")
    print("and the output stays sorted. Duplicate rule: left subtree.")
    print()

    # --- Edge case: search in an empty tree -----------------------------
    print("--- Edge case: searching in an empty tree ---")
    print(f"search(None, 1) -> {search(None, 1)}  (expected: None)")
    print()

    print("=" * 60)
    print("All BST demo cases verified. Learner practice is pending.")
    print("=" * 60)


if __name__ == "__main__":
    main()


