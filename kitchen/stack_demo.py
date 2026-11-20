"""Week 12: watch the call stack wind up and unwind."""

from kitchen.orders import make_orders
from kitchen.recursive import traced_total


def main() -> None:
    orders = make_orders(3)
    print("Final answer:", traced_total(orders))


if __name__ == "__main__":
    main()
