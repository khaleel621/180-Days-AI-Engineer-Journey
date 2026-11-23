"""
day24_shop package: a small shop billing project.

Topic: Modules and Packages - __init__.py.

What is __init__.py?
--------------------
- __init__.py makes a folder a Python package so you can write
  `import day24_shop` and `from day24_shop import ...`.
- Code in __init__.py runs the first time the package is imported.
- It is the right place to re-export the most useful names so users of the
  package do not have to dig into every sub-module.

In this package we re-export:
    get_product, list_products        (from products.py)
    calculate_total, apply_discount   (from billing.py)
    format_receipt                    (from receipt.py)

Because of these imports, both of the following work:

    import day24_shop
    day24_shop.calculate_total([101, 102])

    from day24_shop import calculate_total, apply_discount
    calculate_total([101, 102])

Note: Python 3.3+ also supports "namespace packages" without __init__.py,
but this course uses explicit __init__.py files (regular packages) because
they are clearer for beginners and work in every Python version.
"""

from .products import get_product, list_products
from .billing import calculate_total, apply_discount
from .receipt import format_receipt

# __all__ tells `from day24_shop import *` which names to export.
# Using __all__ is clearer than importing everything with `*`.
__all__ = [
    "get_product",
    "list_products",
    "calculate_total",
    "apply_discount",
    "format_receipt",
]
