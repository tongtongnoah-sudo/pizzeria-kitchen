"""Week 10: what happens to each lookup when n doubles?"""

import matplotlib.pyplot as plt

from kitchen.lookup import count_same_item_pairs, find_order, first_order
from kitchen.orders import make_orders
from kitchen.timing import best_time, growth_factors

MULTIPLIERS = [1, 2, 4, 8]


def time_first(n: int) -> float:
    orders = make_orders(n)  # Build the data OUTSIDE the timer.
    return best_time(lambda: first_order(orders), number=10_000)


def time_find(n: int) -> float:
    orders = make_orders(n)
    # No order has id -1, so find_order must check every order: the worst case.
    return best_time(lambda: find_order(orders, -1), number=100)


def time_pairs(n: int) -> float:
    orders = make_orders(n)
    return best_time(lambda: count_same_item_pairs(orders), number=3)


def main() -> None:
    results = [
        ("first_order", [time_first(1_000 * m) for m in MULTIPLIERS]),
        ("find_order", [time_find(1_000 * m) for m in MULTIPLIERS]),
        ("count_same_item_pairs", [time_pairs(100 * m) for m in MULTIPLIERS]),
    ]

    print(f"{'n grows by:':<33} {MULTIPLIERS}")
    for label, times in results:
        factors = [round(f, 1) for f in growth_factors(times)]
        print(f"{label:<22} slower by: {factors}")
        plt.plot(MULTIPLIERS, factors, marker="o", label=label)

    plt.xlabel("Input size (multiples of the smallest n)")
    plt.ylabel("Time (multiples of the smallest run)")
    plt.title("Kitchen lookups: what happens when n doubles?")
    plt.legend()
    plt.savefig("kitchen_growth.png")
    print("Saved kitchen_growth.png")


if __name__ == "__main__":
    main()
