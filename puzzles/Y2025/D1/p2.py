from typing import Any


def puzzle(input: str) -> Any:
    dial = 50
    zeros = 0
    lines = input.splitlines()
    for line in lines:
        direction = line[0]
        sign = 1 if direction == "R" else -1
        number = int(line[1:])
        # handle full rotations
        full_rotations = number // 100
        zeros += abs(full_rotations)
        remaining = number % 100
        new_dial = dial + remaining * sign
        # another zero if we
        # * wrap around (but don't count if we start on zero)
        # * land on zero
        if dial != 0 and (
            (sign == -1 and new_dial <= 0) or (sign == 1 and new_dial >= 100)
        ):
            zeros += 1
        dial = new_dial % 100
    return zeros
