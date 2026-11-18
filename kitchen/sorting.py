"""Putting the kitchen's orders in order."""

from kitchen.orders import Order, make_orders


def selection_sort_by_total(orders: list[Order]) -> tuple[list[Order], int]:
    """O(n^2). Returns (a new list sorted by total_cents, comparisons made)."""
    remaining = list(orders)
    result: list[Order] = []
    comparisons = 0
    while remaining:
        smallest = remaining[0]
        for i in range(1, len(remaining)):
            comparisons += 1
            if remaining[i].total_cents < smallest.total_cents:
                smallest = remaining[i]
        result.append(smallest)
        remaining.remove(smallest)
    return result, comparisons


pizza_orders = make_orders(10)
pizza_orders_final = selection_sort_by_total(pizza_orders)
print(pizza_orders_final)
