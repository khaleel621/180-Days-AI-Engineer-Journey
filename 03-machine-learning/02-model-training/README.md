# Model Training

## Status: Completed

Practiced the basic scikit-learn Iris classification workflow.

### Script

| File | Description |
|------|-------------|
| `iris-classification.py` | Loads Iris, separates features/labels, train/test split, trains Logistic Regression, prints training accuracy |

### What Was Practiced
- Loading the Iris dataset from `sklearn.datasets`
- Separating features (X) and labels (y)
- Train/test split using `train_test_split`
- Training a Logistic Regression model with `LogisticRegression.fit()`
- Evaluating training accuracy with `accuracy_score`

### How to Run

```bash
python iris-classification.py
```

### Expected Output

```
Iris Classification — Model Training
========================================
Dataset: Iris (150 samples, 4 features, 3 classes)
Classes: ['setosa', 'versicolor', 'virginica']
Train set size: 120
Test set size: 30
Training accuracy: 0.9750
Model: Logistic Regression (max_iter=200)
```

The observed training accuracy was 0.9750 in a verification run using Python 3.13.9 and scikit-learn 1.9.1. Results may differ with other dependency versions or configurations.
