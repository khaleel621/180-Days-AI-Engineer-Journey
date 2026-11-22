# Day 23 Report — Python OOP Composition & DSA Binary Tree Traversals

## Date: 2026-11-22

## Topics Covered

### Track A — Python: OOP Composition

- Composition: one class (the "whole") holds an object of another class (the "part") as an attribute — a "has-a" relationship.
- Why we use composition: code reuse, small focused classes, loose coupling, and swappable parts at runtime.
- Inheritance ("is-a") vs composition ("has-a"): inheritance is tightly coupled; composition is loosely coupled. Prefer composition unless there is a clear "is-a" relationship.
- How one class contains an object of another class: create the part object inside the whole class's `__init__` and store it as `self.<attribute>`, then call the part's methods from the whole.
- Real-world examples implemented in `01-python-fundamentals/day23-composition.py`:
  1. Car and Engine — a Car has an Engine.
  2. Library and Book — a Library has a list of Book objects.
  3. Student and Address — a Student has an Address.
  4. Room, Lamp and Fan — a Room has a Lamp and a Fan.
- Beginner-friendly comments, practical exercises and a `main()` demo with expected outputs are included.
- Edge cases handled: car with no engine, empty library, invalid brand/model input.

### Track B — DSA: Binary Trees — Introduction and Traversals

- Binary tree: each node has at most two children (left and right).
- Root (no parent), parent (has children), child (below a parent), leaf (no children).
- Height: edges on the longest path from a node down to a leaf (empty tree = -1, single node = 0).
- Depth: edges from the root to a node (root = 0).
- Three traversals implemented as separate recursive functions in `02-data-structures-algorithms/trees/day23-binary-tree-traversals.py`:
  1. Inorder (Left, Root, Right)
  2. Preorder (Root, Left, Right)
  3. Postorder (Left, Right, Root)
- Example tree:

        1
       / \
      2   3
     / \
    4   5

  - Inorder:   [4, 2, 5, 1, 3]
  - Preorder:  [1, 2, 4, 5, 3]
  - Postorder: [4, 5, 2, 3, 1]
- Edge cases tested: empty tree, single-node tree, larger (7-node) tree.

### Track C — Machine Learning: Iris Model Evaluation (In Progress)

- Continued the existing Iris project in `03-machine-learning/` (no duplicate project created, AI Journey Day 3 not started).
- The existing Iris evaluation script already covers accuracy, confusion matrix, precision, recall, F1-score, and classification report for the multiclass Iris problem.
- Iris Model Evaluation remains **In Progress** pending your personal review and confirmation. scikit-learn is not installed in this environment, so the Iris script/tests cannot be executed here (pre-existing blocker documented in PROGRESS.md).

## Files Created

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/day23-composition.py` | Source: composition examples + exercises + `main()` demo |
| `01-python-fundamentals/test_day23_composition.py` | Tests for composition (16 tests) |
| `02-data-structures-algorithms/trees/day23-binary-tree-traversals.py` | Source: BinaryTreeNode, traversals, height/depth, edge cases |
| `02-data-structures-algorithms/trees/test_day23_binary_tree_traversals.py` | Tests for binary tree traversals (15 tests) |
| `learning-logs/2026/2026-11-22.md` | Learning log for Day 23 |
| `reports/DAY_23_REPORT.md` | This report |

## Files Modified

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/README.md` | Added Day 23 exercise row + learner-practice-pending entry |
| `02-data-structures-algorithms/README.md` | Added Day 23 trees rows (file inventory + how-to-run) |
| `PROGRESS.md` | Added Day 23 Python + DSA entries; Iris Model Evaluation remains In Progress |

## Test Results

All tests executed and verified (Python 3.11.9, pytest 9.2.0):
- `01-python-fundamentals/test_day23_composition.py`: **16 tests passed**
- `02-data-structures-algorithms/trees/test_day23_binary_tree_traversals.py`: **15 tests passed**
- Combined via pytest: **31 passed, 0 failed**

## Practice Completion Status

| Track | Topic | Status |
|-------|-------|--------|
| Python | Day 23 OOP Composition | Files created, tests verified (16 passed). **Learner practice pending.** |
| DSA | Day 23 Binary Trees — Introduction and Traversals | Files created, tests verified (15 passed). **Learner practice pending.** |
| ML | Iris Model Evaluation | Script complete. **In Progress** — pending your personal review and confirmation. |

Personal practice is NOT marked complete. It remains pending until you confirm completion.

Important: Iris Model Evaluation must remain In Progress until you personally confirm you understand the evaluation results. Do not mark Day 3 of the AI Engineer Journey or any future topic as completed.

## X / Twitter Learning-in-Public Post

Day 23 of my 180-day journey: this repository now covers Python OOP Composition for beginners ("has-a" vs inheritance) and DSA Binary Trees with inorder, preorder and postorder traversals. Code, exercises and tests added; all 31 tests verified. Personal learner practice still pending. #Python #DSA #AIEngineer #LearningInPublic