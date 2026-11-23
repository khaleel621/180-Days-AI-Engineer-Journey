"""
Day 24 helper module: billing (inside the day24_shop package).

Topic: Modules and Packages.

This module handles shopping-cart totals and discounts. It imports
get_product() and product_price() from the products module in the same
package:

    from .products import get_product, product_price

The leading dot means "import products from the same package (day24_shop)".
This is how one module inside a package uses code from another module.
"""

from .products import get_product, product_price


def calculate_total(cart):
    """
    Calculate the total price of a shopping cart.

    Args:
        cart: A list of product ids, for example [101, 102, 101].

    Returns:
        The total price as a float. Unknown product ids are skipped
        with a printed message instead of crashing the whole program.
    """
    total = 0.0
    for product_id in cart:
        price = product_price(product_id)
        if price is None:
            # Beginner-friendly: warn about a bad id but keep going.
            print(f"Warning: product id {product_id} not found, skipping it.")
            continue
        total += price
    return total


def apply_discount(total, discount_percent):
    """
    Apply a percentage discount to a total.

    Args:
        total: The current total amount (float).
        discount_percent: Discount percentage (0 to 100).

    Returns:
        The discounted total as a float.

    Raises:
        ValueError: If discount_percent is not between 0 and 100.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100 percent.")
    discount_amount = total * (discount_percent / 100)
    return total - discount_amount


if __name__ == "__main__":
    # Quick manual demo when this module is run directly.
    cart = [101, 102, 103]
    total = calculate_total(cart)
    print(f"Cart {cart} total = ${total}")
    discounted = apply_discount(total, 10)
    print(f"After 10% discount = ${discounted}")
