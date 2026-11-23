"""
Day 24 helper module: products (inside the day24_shop package).

Topic: Modules and Packages.

This module is one part of a small shop project. It holds the product
catalog and product-related helpers. Other modules (for example billing.py)
import functions from this module, which demonstrates how modules work
together inside a package.

A module is simply a Python file (.py) that contains variables, functions,
and classes you can reuse in other files.
"""

# Product catalog: product_id -> {"name": ..., "price": ...}
# In a real shop this would come from a database; here it is a dictionary
# so the example stays beginner-friendly and self-contained.
PRODUCTS = {
    101: {"name": "Apple",  "price": 0.50},
    102: {"name": "Bread",  "price": 2.00},
    103: {"name": "Milk",   "price": 1.50},
    104: {"name": "Eggs",   "price": 3.00},
    105: {"name": "Butter", "price": 4.00},
}


def get_product(product_id):
    """
    Return the product dictionary for `product_id`, or None if not found.

    Args:
        product_id: The id of the product to look up.

    Returns:
        A dictionary like {"name": "Apple", "price": 0.5}, or None.
    """
    # .dict.get(key) returns None when the key is missing instead of crashing.
    return PRODUCTS.get(product_id)


def product_price(product_id):
    """
    Return the price of `product_id`, or None if the product does not exist.

    Args:
        product_id: The id of the product.

    Returns:
        The price as a float, or None when the product id is unknown.
    """
    product = get_product(product_id)
    if product is None:
        return None
    return product["price"]


def list_products():
    """Return a list of all (product_id, name, price) tuples in the catalog."""
    return [
        (product_id, info["name"], info["price"])
        for product_id, info in PRODUCTS.items()
    ]


if __name__ == "__main__":
    # Quick manual demo when this module is run directly.
    print("Product catalog:")
    for product_id, name, price in list_products():
        print(f"  {product_id}: {name} - ${price}")
    print("Price of 101:", product_price(101))
    print("Price of 999:", product_price(999))
