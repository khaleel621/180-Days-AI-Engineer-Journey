"""
Iris Classification — Model Training
Day 2 — 2026-10-20
Machine Learning

This script practices the basic scikit-learn Iris workflow:
1. Load the Iris dataset.
2. Separate features (X) and labels (y).
3. Split into train/test sets.
4. Train a Logistic Regression model.
5. Print the training accuracy.

Status: Practiced (completed per learning history).
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data      # Features: sepal length, sepal width, petal length, petal width
y = iris.target    # Labels: 0 = setosa, 1 = versicolor, 2 = virginica

# 2. Features and labels are already separated above (X and y)

# 3. Train/test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train Logistic Regression
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 5. Evaluate on training data
train_predictions = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_predictions)

print("Iris Classification — Model Training")
print("=" * 40)
print(f"Dataset: Iris ({len(X)} samples, {X.shape[1]} features, {len(iris.target_names)} classes)")
print(f"Classes: {list(iris.target_names)}")
print(f"Train set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Training accuracy: {train_accuracy:.4f}")
print(f"Model: Logistic Regression (max_iter=200)")