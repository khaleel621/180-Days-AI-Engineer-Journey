# Model Evaluation

## Status: In Progress

The Iris model evaluation script ran successfully in a verification session on 2026-10-23 using Python 3.13.9 and scikit-learn 1.9.1. Your personal review of the metrics and completion of the learning exercise remain pending, so the exercise is still In Progress.

### Script

| File | Description |
|------|-------------|
| `iris-classification-evaluation.py` | Full Iris evaluation: load data, split, train Logistic Regression, predict, accuracy, confusion matrix, classification report |

### What the Script Does
1. Loads the Iris dataset
2. Separates features (X) and labels (y)
3. Performs train/test split (80/20)
4. Trains a Logistic Regression model
5. Generates predictions on the test set
6. Calculates test accuracy
7. Prints the confusion matrix
8. Prints the classification report (precision, recall, F1-score)

### Verification Status
- Execution, test accuracy, confusion matrix, and classification report were verified in the 2026-10-23 session.
- Test accuracy observed in that run: **1.0000** on 30 test samples. This is an observed result, not a guarantee across environments.
- The existing tests check broader conditions and do not assert an exact accuracy value.
- Your personal review of the metrics and completion of the learning exercise remain pending.

### Evaluation Metrics Explained

| Metric | Simple Explanation |
|--------|-------------------|
| **Accuracy** | The proportion of all predictions that are correct. (Correct predictions / Total predictions) |
| **Confusion Matrix** | A table showing, for each class, how many samples were predicted correctly vs. incorrectly. Rows = true class, columns = predicted class. |
| **Precision** | Of all samples predicted as a given class, how many were actually that class? (True Positives / Predicted Positives) |
| **Recall** | Of all samples that actually belong to a given class, how many did we correctly identify? (True Positives / Actual Positives) |
| **F1-Score** | The harmonic mean of precision and recall — a balanced measure when you care about both false positives and false negatives. |

### How to Run

```bash
python iris-classification-evaluation.py
```

### Learner Review Exercise (Personal Review — Pending)

Before marking this exercise complete, personally review and answer the following using the **actual output** from running the script:

1. **Test accuracy:** What is the test accuracy shown in the output? What fraction of the 30 test samples were predicted correctly?
2. **Confusion matrix diagonal:** Look at the diagonal cells (top-left to bottom-right). What do these numbers represent? How many correct predictions does each class have?
3. **Lowest recall class:** Which class (setosa, versicolor, or virginica) has the lowest recall value? What does low recall mean for that class?
4. **Meaning of support:** In the classification report, what does the "support" column represent for each class? Does the support add up to the total test set size?
5. **Why accuracy alone may be insufficient:** If accuracy is 100% (all correct), could there still be a problem the model has with a specific class? When would precision or recall matter more than accuracy?

**Important:** You must supply your own answers to these questions. The assistant cannot claim you have reviewed or understood the metrics unless you have provided your responses.

Until your personal review is complete, this exercise remains **In Progress**. Do not mark Day 3 complete or start it.
