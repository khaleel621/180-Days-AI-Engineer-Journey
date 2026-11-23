"""
Day 24 helper module: receipt (inside the day24_shop package).

Topic: Modules and Packages.

This module formats a printed receipt. It keeps display logic separate from
product data (products.py) and money math (billing.py), which is exactly why
we split a project into modules: each module has one clear job.
"""


def format_receipt(customer_name, cart, total):
    """
    Build a receipt text for a customer's cart.

    Args:
        customer_name: Name of the customer.
        cart: List of product ids.
        total: Final total amount (float).

    Returns:
        A multi-line receipt string.
    """
    lines = []
    lines.append("---- SHOP RECEIPT ----")
    lines.append(f"Customer: {customer_name}")
    lines.append("Items:")
    for product_id in cart:
        # Import locally to avoid a circular import (receipt does not need
        # products at module load time; it only needs them here).
        from .products import get_product
        product = get_product(product_id)
        if product is None:
            lines.append(f"  id {product_id}: unknown product")
        else:
            lines.append(f"  {product['name']}: ${product['price']}")
    lines.append("----------------------")
    lines.append(f"Total: ${total:.2f}")
    lines.append("Thank you for shopping with us!")
    return "\n".join(lines)


if __name__ == "__main__":
    # Quick manual demo when this module is run directly.
    print(format_receipt("Ada", [101, 102], 2.50))
