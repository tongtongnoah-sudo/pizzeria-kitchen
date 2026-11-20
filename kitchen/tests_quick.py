"""Quick checks for the Kitchen Engine. Run: python -m kitchen.tests_quick"""

from kitchen.lookup import binary_lookup, find_order, first_order, linear_lookup
from kitchen.orders import make_orders
from kitchen.recursive import (
    count_item,
    find_order_recursive,
    total_cents,
    total_cents_loop,
)
from kitchen.sorting import selection_sort_by_total

orders = make_orders(10)

# Week 10
assert first_order(orders).order_id == 1000
assert find_order(orders, 1005) == orders[5]
assert find_order(orders, -1) is None

print("Quick checks passed")

# Week 11
assert linear_lookup(orders, -1) == (None, 10)
assert binary_lookup(make_orders(100), 1099)[1] == 7
ranked, comparisons = selection_sort_by_total(orders)
totals = [order.total_cents for order in ranked]
assert comparisons == 45 and totals == sorted(totals)

# Week 12
assert total_cents(orders) == total_cents_loop(orders)
assert find_order_recursive(orders, 1005) == orders[5]
assert find_order_recursive(orders, -1) is None
assert count_item(make_orders(50), "veggie") == 14
