"""Week 12: kitchen loops rewritten as recursion."""

from kitchen.orders import Order


def total_cents_loop(orders: list[Order]) -> int:
    """The iterative version we are converting."""
    total = 0
    for order in orders:
        total += order.total_cents
    return total


def total_cents(orders: list[Order]) -> int:
    """The total of a list is its first order plus the total of the rest."""
    if not orders:
        return 0
    else:
        return orders[0].total_cents + total_cents(orders[1:])


def traced_total(orders: list[Order], depth: int = 0) -> int:
    """total_cents with print statements that show the call stack."""
    indent = "    " * depth
    ids = [order.order_id for order in orders]
    print(f"{indent}call   total_cents({ids})")
    if not orders:
        print(f"{indent}base case -> 0")
        return 0
    else:
        rest = traced_total(orders[1:], depth + 1)
        result = orders[0].total_cents + rest
        print(f"{indent}return {orders[0].total_cents} + {rest} = {result}")
        return result


def find_order_recursive(orders: list[Order], order_id: int) -> Order | None:
    """Recursive version of find_order from Week 10."""
    if not orders:
        return None
    elif orders[0].order_id == order_id:
        return orders[0]
    else:
        result = find_order_recursive(orders[1:], order_id)
        return result


def count_item(orders: list[Order], item: str) -> int:
    """Recursive function to count orders for given item."""
    if not orders:
        return 0
    else:
        return count_item(orders[1:], item) + int(orders[0].item == item)
