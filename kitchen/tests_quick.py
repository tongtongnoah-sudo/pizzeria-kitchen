"""Quick checks for the Kitchen Engine. Run: python -m kitchen.tests_quick"""

from kitchen.lookup import find_order, first_order
from kitchen.orders import make_orders

orders = make_orders(10)

# Week 10
assert first_order(orders).order_id == 1000
assert find_order(orders, 1005) == orders[5]
assert find_order(orders, -1) is None

print("Quick checks passed")
