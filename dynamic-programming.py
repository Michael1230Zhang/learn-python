# pyright: strict

from functools import cache


@cache
def ways(stairs: int) -> int:
    match stairs:
        case 1: return 1
        case 2: return 2
        case _: return ways(stairs - 2) + ways(stairs - 1)


@cache
def fib(n: int) -> int:
    match n:
        case 0: return 0
        case 1: return 1
        case _: return fib(n - 2) + fib(n - 1)
