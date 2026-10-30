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
