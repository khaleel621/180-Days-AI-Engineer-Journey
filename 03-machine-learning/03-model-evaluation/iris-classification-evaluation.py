"""
Iris Classification — Model Evaluation
Day 2 — 2026-10-20
Machine Learning

This script evaluates a Logistic Regression model on the Iris dataset.
It extends the training workflow with full evaluation metrics.

Components included:
- Loading the Iris dataset
- Separating features (X) and labels (y)
- Train/test split
- Training Logistic Regression
- Generating predictions on the test set
- Calculating accuracy
- Printing the confusion matrix
- Printing the classification report

Status: Execution and outputs verified in a separate session on 2026-10-23
using Python 3.13.9 and scikit-learn 1.9.1. Test accuracy observed in that
run: 1.0000; results may vary across environments. The learner's personal
review of the metrics and exercise completion remain pending.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

# 5. Generate predictions on the test set
y_pred = model.predict(X_test)

# 6. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# 7. Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# 8. Classification report
class_report = classification_report(y_test, y_pred, target_names=iris.target_names)

print("Iris Classification — Model Evaluation")
print("=" * 45)
print(f"Dataset: Iris ({len(X)} samples, {X.shape[1]} features, {len(iris.target_names)} classes)")
print(f"Classes: {list(iris.target_names)}")
print(f"Train set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")
print(f"Model: Logistic Regression (max_iter=200)")
print()
print(f"Test Accuracy: {accuracy:.4f}")
print()
print("Confusion Matrix:")
print(conf_matrix)
print()
print("Classification Report:")
print(class_report)
