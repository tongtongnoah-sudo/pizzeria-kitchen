"""Answering the kitchen's most common question: where is this order?"""

from kitchen.orders import Order


def first_order(orders: list[Order]) -> Order:
    """O(1): reading index 0 is one step, however long the list is."""
    return orders[0]


def find_order(orders: list[Order], order_id: int) -> Order | None:
    """O(n): in the worst case, every order is checked once."""
    for order in orders:
        if order.order_id == order_id:
            return order
    return None


def count_same_item_pairs(orders: list[Order]) -> int:
    """O(n^2): every order is compared with every later order."""
    pairs = 0
    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            if orders[i].item == orders[j].item:
                pairs += 1
    return pairs


def linear_lookup(
    orders: list[Order],
    order_id: int,
) -> tuple[Order | None, int]:
    """O(n). Returns (the order or None, how many orders were checked)."""
    probes = 0
    for order in orders:
        probes += 1
        if order.order_id == order_id:
            return order, probes
    return None, probes


def binary_lookup(
    orders: list[Order],
    order_id: int,
) -> tuple[Order | None, int]:
    """O(log n). The orders must be sorted by order_id."""
    low = 0
    high = len(orders) - 1
    probes = 0
    while low <= high:  # <=, so the last candidate still gets checked
        mid = (low + high) // 2  # // keeps mid an int; / would make a float
        probes += 1
        guess = orders[mid]
        if guess.order_id == order_id:
            return guess, probes
        elif guess.order_id > order_id:
            high = mid - 1
        else:
            low = mid + 1
    return None, probes
