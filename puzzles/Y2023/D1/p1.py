from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    sum = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                sum += int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                sum += int(char)
                break
    return sum
