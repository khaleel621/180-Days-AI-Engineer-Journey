"""
Day 9 — Data Structures & Algorithms: Best Time to Buy and Sell Stock

Topic: Arrays — Single-pass maximum profit

Problem:
    Given a list of daily stock prices, find the maximum profit possible
    by buying once and selling on a later day. If no profit is possible,
    return 0.

Approach — Single pass:
    Keep track of the minimum price seen so far and the maximum profit
    achievable. For each price:
      1. Calculate profit = current price - minimum_price (the best profit
         if we sell today, having bought at the lowest earlier price).
      2. Update maximum_profit if this profit is higher.
      3. Update minimum_price if the current price is lower.

    This is a single pass through the list: O(n) time, O(1) extra space.

Why the buy day must be before the sell day:
    You cannot sell a stock before you buy it. The algorithm only considers
    selling at the current price after having seen (and potentially bought at)
    an earlier price, because minimum_price is always the lowest price seen
    *before* the current index.

Why the minimum price is updated during traversal:
    As we scan forward, a lower price may appear. Buying at that lower price
    could unlock a larger profit on a future day, so we keep minimum_price
    updated to the smallest value seen so far.

Time complexity: O(n) — one pass through the prices list.
Extra space complexity: O(1) — only minimum_price and maximum_profit.

Examples:
    max_profit([7, 1, 5, 3, 6, 4]) -> 5   (buy at 1, sell at 6)
    max_profit([7, 6, 4, 3, 1])    -> 0   (prices only go down)
    max_profit([2, 4, 1])          -> 2   (buy at 2, sell at 4)
    max_profit([3])                -> 0   (only one day, cannot sell later)
    max_profit([])                 -> 0   (no prices)
    max_profit([1, 1])             -> 0   (no price increase)
"""


def max_profit(prices):
    """
    Find the maximum profit from buying once and selling on a later day.

    Uses a single pass. Tracks the minimum price seen so far and the best
    profit achievable. If no profit is possible, returns 0.

    Args:
        prices: A list of daily stock prices (ints or floats).

    Returns:
        The maximum profit possible, or 0 if no profit can be made.

    Example:
        max_profit([7, 1, 5, 3, 6, 4]) -> 5
    """
    # Edge cases: empty list or a single price cannot produce a profit
    # because there is no later day to sell on.
    if len(prices) < 2:
        return 0

    # Initialize with the first price: the earliest possible buy price.
    minimum_price = prices[0]
    maximum_profit = 0

    # Start from the second price (index 1) — we need at least one earlier
    # price to buy at before we can sell at the current price.
    for i in range(1, len(prices)):
        current_price = prices[i]

        # Profit if we bought at minimum_price (an earlier day) and sell today.
        profit = current_price - minimum_price

        # Keep the best profit seen so far.
        if profit > maximum_profit:
            maximum_profit = profit

        # Update the minimum price if today's price is lower, so future
        # days can potentially buy at an even lower price.
        if current_price < minimum_price:
            minimum_price = current_price

    return maximum_profit


def main():
    examples = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [2, 4, 1],
        [3],
        [],
        [1, 1],
    ]

    print("Best Time to Buy and Sell Stock — examples:")
    print("=" * 50)
    for prices in examples:
        result = max_profit(prices)
        print(f"  max_profit({prices}) -> {result}")


if __name__ == "__main__":
    main()