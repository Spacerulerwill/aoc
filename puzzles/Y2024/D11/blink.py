from functools import cache
from typing import Iterable


@cache
def blink_stone(stone: int, n: int) -> int:
    # base case
    if n == 0:
        return 1
    if stone == 0:
        size = blink_stone(1, n - 1)
    elif len(str(stone)) % 2 == 0:
        str_num = str(stone)
        half = len(str_num) // 2
        first_half = int(str_num[:half])
        second_half = int(str_num[half:])
        size = blink_stone(first_half, n - 1) + blink_stone(second_half, n - 1)
    else:
        size = blink_stone(stone * 2024, n - 1)
    return size


def blink_stones(stones: Iterable[int], n: int) -> int:
    return sum(blink_stone(stone, n) for stone in stones)
