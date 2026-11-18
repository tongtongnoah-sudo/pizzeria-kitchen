"""Week 11: count the work each algorithm does as n grows."""

from kitchen.lookup import binary_lookup, linear_lookup
from kitchen.orders import make_orders
from kitchen.sorting import selection_sort_by_total

# Bigger than every real id: the worst case for both searches.
MISSING_ID = 999_999


def main() -> None:
    print(f"{'n':>6} | {'linear':>6} | {'binary':>6} | {'selection':>9}")
    print("-" * 36)
    for n in [10, 100, 1_000]:
        orders = make_orders(n)
        _, linear = linear_lookup(orders, MISSING_ID)
        _, binary = binary_lookup(orders, MISSING_ID)
        _, selection = selection_sort_by_total(orders)
        print(f"{n:>6} | {linear:>6} | {binary:>6} | {selection:>9}")


if __name__ == "__main__":
    main()
