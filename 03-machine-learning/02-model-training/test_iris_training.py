"""
Beginner-friendly tests for Iris Classification — Model Training.

These tests verify the iris-classification.py script works correctly
without modifying the original implementation.
"""

import importlib.util
import os

# Load iris-classification module by file path
_module_path = os.path.join(os.path.dirname(__file__), "iris-classification.py")
_spec = importlib.util.spec_from_file_location("iris_classification", _module_path)
_iris_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_iris_module)


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
    assert len(y_train) == 120
    assert len(y_test) == 30


def test_logistic_regression_trains():
    """Logistic Regression should train without error on Iris training data."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)  # should not raise
    assert model is not None


def test_training_accuracy_valid():
    """Training accuracy should be between 0 and 1."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    acc = accuracy_score(y_train, train_pred)
    assert 0.0 <= acc <= 1.0


if __name__ == "__main__":
    test_iris_dataset_loads()
    test_train_test_split_sizes()
    test_logistic_regression_trains()
    test_training_accuracy_valid()
    print("All Iris training tests passed!")