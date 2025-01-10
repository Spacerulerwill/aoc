from typing import Any


def puzzle(input: str) -> Any:
    numbers = [int(num) for num in input.splitlines()]
    seen = set()
    for num in numbers:
        compliment = 2020 - num
        if compliment in seen:
            return num * compliment
        seen.add(num)
