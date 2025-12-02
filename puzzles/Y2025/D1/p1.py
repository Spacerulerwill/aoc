from typing import Any


def puzzle(input: str) -> Any:
    dial = 50
    zeros = 0
    lines = input.splitlines()
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        multiplier = 1 if direction == "R" else -1
        dial = (dial + number * multiplier) % 100
        if dial == 0:
            zeros += 1
    return zeros
