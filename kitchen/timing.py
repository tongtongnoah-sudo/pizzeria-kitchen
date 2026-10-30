"""Timing helpers shared by every kitchen benchmark."""

import timeit
from collections.abc import Callable


def best_time(func: Callable[[], object], number: int) -> float:
    """Seconds per call, taking the fastest of 5 runs to filter out noise."""
    runs = timeit.repeat(func, number=number, repeat=5)
    return min(runs) / number


def growth_factors(times: list[float]) -> list[float]:
    """How many times slower each measurement is than the first one."""
    return [t / times[0] for t in times]
