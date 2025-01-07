from typing import Any


def puzzle(input: str) -> Any:
    floor = 0
    for char in input:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor
