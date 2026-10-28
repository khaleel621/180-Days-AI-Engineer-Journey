# AI-Engineer-Journey

A 180-day journey to becoming an AI Engineer. This repository tracks my learning progress from Python fundamentals through advanced AI engineering topics.

Alongside the AI topics, I practice Python and Data Structures & Algorithms (DSA) every day:

* **Python Fundamentals** (`01-python-fundamentals/`) — Python language basics: syntax, conditions, loops, input/output, functions, and beginner programs.
* **Data Structures & Algorithms** (`02-data-structures-algorithms/`) — Algorithmic problem-solving and data-structure practice, organized by topic.

Tests are kept alongside the code they cover. Daily notes are in `learning-logs/`, and detailed reports plus unpublished social drafts are in `reports/`.

## Repository Structure

| Folder | Description | Status |
|--------|-------------|--------|
| `01-python-fundamentals/` | Python basics and practice | In Progress |
| `02-data-structures-algorithms/` | DSA with Python | In Progress |
| `03-machine-learning/` | Machine Learning fundamentals | In Progress |
| `04-deep-learning/` | Deep Learning and neural networks | Not Started |
| `05-generative-ai/` | Generative AI | Not Started |
| `06-llm-engineering/` | LLM Engineering | Not Started |
| `07-rag-systems/` | RAG Systems | Not Started |
| `08-agentic-ai/` | Agentic AI | Not Started |
| `09-backend-and-apis/` | Backend and APIs | Not Started |
| `10-deployment-and-mlops/` | Deployment and MLOps | Not Started |
| `11-projects/` | Capstone projects | Not Started |
| `12-interview-preparation/` | Interview preparation | Not Started |
| `13-job-and-internship-preparation/` | Job and internship preparation | Not Started |
| `learning-logs/` | Daily learning logs | In Progress |
| `reports/` | Daily reports and unpublished social drafts | In Progress |

## Python Fundamentals vs Data Structures & Algorithms

**Python Fundamentals** teaches the Python language itself — variables, data types, conditions, loops, input/output, functions, and basic object-oriented programming. These exercises are about learning syntax and language features.

**Data Structures & Algorithms** focuses on problem-solving patterns — arrays, strings, searching, counting, complexity analysis, and so on. These exercises assume you already know basic Python and focus on algorithms and data structures rather than on teaching Python syntax.

Tests for each folder live beside the code they cover in that folder.

## How to Run Python Practice Files

From the repository root, run any exercise file directly with Python:

```bash
python 01-python-fundamentals/01-student-marks-analysis.py
python 01-python-fundamentals/03-multiplication-table.py
python 02-data-structures-algorithms/arrays/two-sum.py
python 02-data-structures-algorithms/day_02-even-odd.py
```

`03-multiplication-table.py` and `day_02-even-odd.py` read input from the keyboard (`input()`), so run them in an interactive terminal and type a value when prompted.

## How to Run Tests

The repository's test files use plain Python assert statements with an if __name__ == "__main__" runner, so they run directly with Python. Python's built-in unittest module is available, but these test files are designed to be executed directly:

```bash
python 01-python-fundamentals/test_student_marks.py
python 01-python-fundamentals/test_student_marks_oop.py
python 02-data-structures-algorithms/arrays/day01_test_two_sum.py
```

## Current Progress (Verified)

* **Day 1 — 2026-10-19: Student Marks Analysis** — Dictionary storage, average, topper, pass/fail counts, plus Student and MarksBook OOP classes (__init__, self). Verified: test_student_marks.py and test_student_marks_oop.py pass.
* **Day 2 — 2026-10-20: Two Sum** — Nested-loop solution in 02-data-structures-algorithms/arrays/two-sum.py. Verified: day01_test_two_sum.py passes.
* **Day 5 — 2026-10-28: Python Functions + DSA Counting Occurrences** — `add_numbers(a, b)` in `01-python-fundamentals/day05-functions.py` (verified: `Sum: 30`, tests pass) and `count_occurrences(numbers, target)` in `02-data-structures-algorithms/arrays/day05-count-occurrences.py` (verified: `2 appears 3 times`, O(n) time, O(1) extra space, tests pass).
* **Day 2 Practice Continuation — 2026-10-25: Even/Odd and Multiplication Table** — day_02-even-odd.py and 03-multiplication-table.py implemented and behavior verified. Note: test_day02-conditions-loops.py still references 02-even-odd.py, which was removed during reorganization, so that test currently raises FileNotFoundError until its reference is updated.
* **DSA array counting** — test_count_even_numbers.py references count-even-numbers.py, which is no longer present, so that test currently raises FileNotFoundError until the solution file is restored or the reference corrected.

Days 3 onward are not started unless explicitly recorded in PROGRESS.md.

## Documentation

* [PROGRESS.md](PROGRESS.md) — Detailed progress tracking
* [ROADMAP.md](ROADMAP.md) — 180-day AI Engineering roadmap
* [01-python-fundamentals/README.md](01-python-fundamentals/README.md) — Python fundamentals exercises
* [02-data-structures-algorithms/README.md](02-data-structures-algorithms/README.md) — DSA exercises
* [learning-logs/2026/](learning-logs/2026/) — Daily learning logs
* [reports/](reports/) — Daily reports and unpublished social drafts

