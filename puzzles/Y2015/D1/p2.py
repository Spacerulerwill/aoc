from typing import Any


def puzzle(input: str) -> Any:
    floor = 0
    position = 0
    while floor != -1:
        char = input[position]
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        position += 1
    return position
