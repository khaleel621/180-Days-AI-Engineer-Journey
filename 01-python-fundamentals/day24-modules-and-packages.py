"""
Day 24 - Python Fundamentals: Modules and Packages

Topic: Modules and Packages

This file teaches beginner-friendly module and package concepts using a
small real-world project: a shop billing package (folder day24_shop/) that
contains several modules working together.

================================================================================
1. WHAT IS A PYTHON MODULE?
================================================================================
A module is a Python file (ending in .py) that contains definitions you can
reuse: variables, functions, classes, and constants.

Examples you already know: math, random. Examples we write ourselves:
math_operations.py (Day 14) and the modules inside day24_shop/ (Day 24).

================================================================================
2. WHY DO WE USE MODULES?
================================================================================
- Reuse: write code once, use it in many files.
- Organization: split a big project into small files with one job each.
- Maintainability: fix a bug in one module instead of hunting through one
  giant file.
- Collaboration: different people can work on different modules.

================================================================================
3. CREATING OUR OWN MODULE
================================================================================
Any .py file you write becomes a module. The files inside day24_shop/ are
modules we created:
    products.py    - the product catalog
    billing.py     - cart totals and discounts
    receipt.py     - receipt formatting

Each module has one clear job.

================================================================================
4. IMPORTING MODULES WITH `import`
================================================================================
import day24_shop
day24_shop.calculate_total([101, 102])

The whole module/package is loaded; you call its contents with the module
name as a prefix: module_name.function().

================================================================================
5. IMPORTING SPECIFIC FUNCTIONS WITH `from ... import`
================================================================================
from day24_shop import calculate_total, apply_discount

The named functions are brought into your file and can be called directly,
without the module name prefix.

================================================================================
6. ALIASES WITH `as`
================================================================================
from day24_shop.billing import calculate_total as calc

The `as` keyword gives an imported name a new alias (nickname) in your file.
Useful when the original name is long or clashes with a name you already use.

================================================================================
7. WHAT IS A PYTHON PACKAGE?
================================================================================
A package is a FOLDER that contains modules, marked by an __init__.py file.
day24_shop/ is a package because it has __init__.py plus products.py,
billing.py, and receipt.py.

================================================================================
8. MODULE VS PACKAGE
================================================================================
|                      | Module                 | Package                   |
|----------------------|------------------------|---------------------------|
| What is it?          | A single .py file      | A folder of .py files     |
| Example              | products.py            | day24_shop/               |
| How to import        | import products        | import day24_shop         |
| Contains             | functions, classes...  | modules + __init__.py     |

Every package is made of modules; a module is not a package.

================================================================================
9. UNDERSTANDING __init__.py
================================================================================
__init__.py turns a folder into a package and runs when the package is first
imported. In day24_shop/__init__.py we re-export the most useful names:

    from .products import get_product, list_products
    from .billing import calculate_total, apply_discount
    from .receipt import format_receipt

Thanks to __init__.py, both `import day24_shop` and
`from day24_shop import calculate_total` work. Without __init__.py the folder
is just a folder (Python 3.3+ namespace packages aside), and those imports
fail in this project's beginner-friendly setup.

================================================================================
10. ORGANIZING A SMALL PROJECT WITH MODULES AND PACKAGES
================================================================================
Project layout used in this file:

    01-python-fundamentals/
    ├── day24-modules-and-packages.py   # this lesson file
    └── day24_shop/                     # a package
        ├── __init__.py                 # makes it a package, re-exports names
        ├── products.py                 # module: product catalog
        ├── billing.py                  # module: totals and discounts
        └── receipt.py                  # module: receipt formatting

billing.py imports from products.py (one module importing another inside a
package): `from .products import get_product, product_price`. The dot means
"from the same package". This keeps each module focused while letting them
work together.

Day 14 taught importing from ONE custom module (math_operations.py). Day 24
goes further: a whole PACKAGE of modules that import from each other.
"""

# ---------------------------------------------------------------------------
# Imports used by the demo below
# ---------------------------------------------------------------------------
import day24_shop                      # Style 4: import the whole package
from day24_shop import apply_discount  # Style 5: import specific functions
from day24_shop.billing import calculate_total as calc  # Style 6: alias
import day24_shop.products             # Importing a module inside a package


def demo_shop_package():
    """
    Run the shop demo and return the results as strings.

    Demonstrates:
        - import package (style 4)
        - from ... import (style 5)
        - ... as alias (style 6)
        - importing a sub-module of a package
        - functions defined inside package modules
    """
    cart = [101, 102, 103]   # Apple, Bread, Milk

    # Style 4: import package -> day24_shop.calculate_total
    total = day24_shop.calculate_total(cart)
    result_total = f"day24_shop.calculate_total([101, 102, 103]) = ${total}"

    # Style 5: from ... import -> apply_discount directly
    discounted = apply_discount(total, 10)   # 10% off
    result_discounted = f"apply_discount({total}, 10) = ${discounted}"

    # Style 6: ... as -> calc is an alias for calculate_total
    total_again = calc([104, 105])   # Eggs + Butter
    result_alias = f"calc([104, 105]) = ${total_again}"

    # Importing a module inside a package: day24_shop.products.list_products()
    product_list = day24_shop.products.list_products()
    result_products = "day24_shop.products.list_products() = " + str(product_list)

    # Receipt formatting (uses receipt.py, which reads products.py internally)
    receipt_text = day24_shop.format_receipt("Ada", cart, discounted)
    result_receipt = "\n" + receipt_text

    return {
        "total": result_total,
        "discounted": result_discounted,
        "alias": result_alias,
        "products": result_products,
        "receipt": result_receipt,
    }


# ===========================================================================
# DEMO
# ===========================================================================
def main():
    print("=" * 60)
    print("Day 24 - Python Fundamentals: Modules and Packages")
    print("=" * 60)
    print()
    print("Project: a small shop billing package (day24_shop/)")
    print("Modules: products.py, billing.py, receipt.py")
    print("Package glue: __init__.py")
    print()

    # Show the catalog first (real-world context).
    print("--- Product catalog (day24_shop.products) ---")
    for product_id, name, price in day24_shop.products.list_products():
        print(f"  {product_id}: {name} - ${price}")
    print()

    # Run the import-style demo.
    print("--- Import styles demo ---")
    results = demo_shop_package()
    print(results["total"])
    print(results["discounted"])
    print(results["alias"])
    print(results["products"])
    print()

    # Receipt (expected output shown below the demo).
    print("--- Printed receipt ---")
    print(results["receipt"])

    print()
    print("Expected receipt (customer Ada, 10% off Apple+Bread+Milk):")
    print("---- SHOP RECEIPT ----")
    print("Customer: Ada")
    print("Items:")
    print("  Apple: $0.5")
    print("  Bread: $2.0")
    print("  Milk: $1.5")
    print("----------------------")
    print("Total: $3.60")
    print("Thank you for shopping with us!")
    print()

    # --- Beginner mistakes to avoid --------------------------------------
    print("--- Common beginner mistakes ---")
    print("1. ModuleNotFoundError: running the file from the wrong folder. "
          "Run from the repository root.")
    print("2. Forgetting __init__.py: without it, day24_shop/ is not treated "
          "as a package here.")
    print("3. Circular imports: module A imports B and B imports A. Keep each")
    print("   module's job clear (products = data, billing = math, receipt = view).")
    print("4. `from module import *`: avoid it; you cannot tell where names come from.")
    print("5. Confusing module (.py file) with package (folder).")
    print()

    print("=" * 60)
    print("PRACTICAL EXERCISES - try these yourself in the day24_shop package:")
    print("=" * 60)
    print("1. Add a remove_product(product_id) function to products.py that")
    print("   deletes a product from PRODUCTS and add a test for it.")
    print("2. Add a calculate_tax(total, tax_percent) function to billing.py")
    print("   and use it in the receipt demo.")
    print("3. Create a NEW package day24_library/ with books.py and members.py,")
    print("   then import from it in a new script (do not modify day24_shop).")
    print("4. On paper, draw the import flow: lesson file -> day24_shop package ->")
    print("   __init__.py -> billing.py -> products.py. Where does each name live?")
    print()
    print("Learner practice is pending - complete the exercises yourself to mark")
    print("Day 24 complete. Files are intentionally NOT marked complete here.")
    print("=" * 60)


if __name__ == "__main__":
    main()

