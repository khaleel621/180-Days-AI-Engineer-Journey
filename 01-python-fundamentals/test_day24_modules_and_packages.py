"""
Tests for Day 24 - Modules and Packages in
01-python-fundamentals/day24-modules-and-packages.py and the day24_shop package.

Covers:
  - Importing a custom package/module: `import day24_shop`
  - Importing specific functions: `from day24_shop import calculate_total`
  - Aliases with `as`: `from day24_shop.billing import calculate_total as calc`
  - Package structure: __init__.py exists, products.py/billing.py/receipt.py exist
  - Package functionality: calculate_total, apply_discount, format_receipt,
    get_product, list_products work correctly
  - One module inside the package importing another (billing.py imports products.py)
  - The lesson file's demo_shop_package() returns correct results

The day24_shop package lives in the same folder as this test file, so
`import day24_shop` works when this test is run with
`python 01-python-fundamentals/test_day24_modules_and_packages.py`.
The folder is also added to sys.path explicitly so the tests work under pytest.
"""

import importlib.util
import os
import sys

# ---------------------------------------------------------------------------
# Make the package importable (needed when run via pytest as well).
# ---------------------------------------------------------------------------
_here = os.path.dirname(__file__)
if _here not in sys.path:
    sys.path.insert(0, _here)

# ---------------------------------------------------------------------------
# Load the lesson file by file path.
# ---------------------------------------------------------------------------
_lesson_path = os.path.join(_here, "day24-modules-and-packages.py")
_lesson_spec = importlib.util.spec_from_file_location(
    "day24_modules_and_packages", _lesson_path)
_lesson_module = importlib.util.module_from_spec(_lesson_spec)
_lesson_spec.loader.exec_module(_lesson_module)

demo_shop_package = _lesson_module.demo_shop_package

# ---------------------------------------------------------------------------
# Import the package in the styles being tested.
# ---------------------------------------------------------------------------
import day24_shop                                  # import the whole package
from day24_shop import calculate_total, apply_discount  # from ... import
from day24_shop.billing import calculate_total as calc  # ... as alias
from day24_shop.receipt import format_receipt
from day24_shop.products import get_product, list_products, product_price

# ---------------------------------------------------------------------------
# Package structure tests
# ---------------------------------------------------------------------------

def test_package_folder_exists():
    """day24_shop/ must be a folder inside 01-python-fundamentals/."""
    package_dir = os.path.join(_here, "day24_shop")
    assert os.path.isdir(package_dir), "day24_shop package folder is missing"


def test_init_py_exists():
    """__init__.py is what makes day24_shop/ a package."""
    init_path = os.path.join(_here, "day24_shop", "__init__.py")
    assert os.path.isfile(init_path), "__init__.py is missing from day24_shop/"


def test_package_modules_exist():
    """The package contains products.py, billing.py, and receipt.py."""
    for filename in ("products.py", "billing.py", "receipt.py"):
        assert os.path.isfile(os.path.join(_here, "day24_shop", filename)), \
            f"{filename} is missing from day24_shop/"


def test_package_reexports_functions():
    """__init__.py re-exports the most useful names."""
    assert hasattr(day24_shop, "calculate_total")
    assert hasattr(day24_shop, "apply_discount")
    assert hasattr(day24_shop, "format_receipt")
    assert hasattr(day24_shop, "get_product")
    assert hasattr(day24_shop, "list_products")


# ---------------------------------------------------------------------------
# Import style tests (import / from ... import / ... as)
# ---------------------------------------------------------------------------

def test_import_whole_package_style():
    """`import day24_shop` then day24_shop.calculate_total(...) works."""
    assert day24_shop.calculate_total([101]) == 0.5
    assert day24_shop.get_product(102)["name"] == "Bread"


def test_from_import_specific_functions():
    """`from day24_shop import calculate_total, apply_discount` works."""
    assert calculate_total([101, 102]) == 2.5    # 0.5 + 2.0
    assert apply_discount(100.0, 10) == 90.0      # 10% off
    assert apply_discount(100.0, 0) == 100.0      # 0% off
    assert apply_discount(100.0, 100) == 0.0      # 100% off


def test_as_alias_import():
    """`from ... import ... as` gives the function an alias."""
    assert calc([104, 105]) == 7.0               # 3.0 + 4.0


def test_from_import_submodule():
    """Importing from a sub-module of the package works."""
    assert format_receipt("Ada", [101, 102], 2.50) is not None


# ---------------------------------------------------------------------------
# Package functionality tests
# ---------------------------------------------------------------------------

def test_calculate_total_known_cart():
    """calculate_total adds up the prices of known product ids."""
    assert calculate_total([101, 102, 103]) == 4.0   # 0.5 + 2.0 + 1.5
    assert calculate_total([101, 101]) == 1.0        # two Apples


def test_calculate_total_skips_unknown_ids():
    """Unknown product ids are skipped with a warning instead of crashing."""
    total = calculate_total([101, 999, 102])
    assert total == 2.5   # 0.5 + 2.0; 999 skipped


def test_apply_discount_invalid_percent():
    """Discounts outside 0..100 raise ValueError."""
    for bad in (-1, 101):
        try:
            apply_discount(100.0, bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"apply_discount(100, {bad}) did not raise ValueError")


def test_get_product():
    """get_product looks up a product by id."""
    assert get_product(101) == {"name": "Apple", "price": 0.5}
    assert get_product(105) == {"name": "Butter", "price": 4.0}
    assert get_product(999) is None


def test_product_price():
    """product_price returns the price or None for unknown ids."""
    assert product_price(102) == 2.0
    assert product_price(999) is None


def test_list_products():
    """list_products returns every product in the catalog."""
    products = list_products()
    assert len(products) == 5
    ids = [p[0] for p in products]
    assert ids == [101, 102, 103, 104, 105]


def test_format_receipt_content():
    """The receipt contains the customer name, items, and total."""
    receipt = format_receipt("Ada", [101, 102], 2.50)
    assert "Ada" in receipt
    assert "Apple" in receipt
    assert "Bread" in receipt
    assert "$2.50" in receipt


# ---------------------------------------------------------------------------
# Lesson file demo test
# ---------------------------------------------------------------------------

def test_demo_shop_package_results():
    """demo_shop_package() returns correct results for every import style."""
    results = demo_shop_package()
    assert results["total"] == "day24_shop.calculate_total([101, 102, 103]) = $4.0"
    assert results["discounted"] == "apply_discount(4.0, 10) = $3.6"
    assert results["alias"] == "calc([104, 105]) = $7.0"
    assert "(101, 'Apple', 0.5)" in results["products"]
    assert "---- SHOP RECEIPT ----" in results["receipt"]
    assert "Customer: Ada" in results["receipt"]
    assert "Total: $3.60" in results["receipt"]


if __name__ == "__main__":
    test_package_folder_exists()
    test_init_py_exists()
    test_package_modules_exist()
    test_package_reexports_functions()
    test_import_whole_package_style()
    test_from_import_specific_functions()
    test_as_alias_import()
    test_from_import_submodule()
    test_calculate_total_known_cart()
    test_calculate_total_skips_unknown_ids()
    test_apply_discount_invalid_percent()
    test_get_product()
    test_product_price()
    test_list_products()
    test_format_receipt_content()
    test_demo_shop_package_results()
    print("All test_day24_modules_and_packages tests passed!")

