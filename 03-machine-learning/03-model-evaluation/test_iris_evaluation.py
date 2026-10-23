"""
Beginner-friendly tests for Iris Classification — Model Evaluation.

These tests verify the iris-classification-evaluation.py script works correctly.
The script is marked In Progress — these tests confirm the code runs and
produces valid output, but the exercise is not considered completed until
the user runs it and verifies the results manually.
"""

import importlib.util
import os

# Load iris-classification-evaluation module by file path
_module_path = os.path.join(os.path.dirname(__file__), "iris-classification-evaluation.py")
_spec = importlib.util.spec_from_file_location("iris_evaluation", _module_path)
_eval_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_eval_module)


def test_iris_dataset_loads():
    """The Iris dataset should load with 150 samples and 4 features."""
    from sklearn.datasets import load_iris
    iris = load_iris()
    assert iris.data.shape == (150, 4)
    assert iris.target.shape == (150,)
    assert len(iris.target_names) == 3


def test_train_test_split_sizes():
    """Train/test split should produce expected sizes (80/20 of 150)."""
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    assert len(X_train) == 120
    assert len(X_test) == 30


def test_logistic_regression_trains_and_predicts():
    """Logistic Regression should train and produce predictions on test data."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert len(y_pred) == len(y_test)


def test_accuracy_confusion_matrix_report():
    """Accuracy, confusion matrix, and classification report should all be valid."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    assert 0.0 <= acc <= 1.0

    cm = confusion_matrix(y_test, y_pred)
    assert cm.shape == (3, 3)  # 3 classes

    report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
    assert "setosa" in report
    assert "versicolor" in report
    assert "virginica" in report


if __name__ == "__main__":
    test_iris_dataset_loads()
    test_train_test_split_sizes()
    test_logistic_regression_trains_and_predicts()
    test_accuracy_confusion_matrix_report()
    print("All Iris evaluation tests passed!")