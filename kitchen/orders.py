"""Orders for the Pizzeria Kitchen Engine."""

import random
from dataclasses import dataclass

MENU = ("margherita", "pepperoni", "veggie", "hawaiian", "bbq chicken")


@dataclass(frozen=True)
class Order:
    """One ticket from the order screen."""

    order_id: int
    item: str
    total_cents: int
    minute: int


def make_orders(n: int, seed: int = 42) -> list[Order]:
    """Return n orders in arrival order: ids and minutes both ascend."""
    rng = random.Random(seed)
    return [
        Order(
            order_id=1000 + i,
            item=rng.choice(MENU),
            total_cents=rng.randrange(899, 4599),
            minute=i,
        )
        for i in range(n)
    ]
