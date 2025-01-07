from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.strip().split("\n")]
    total = 0
    for line in lines:
        measurements = [int(measurement) for measurement in line.split("x")]
        side1 = measurements[0] * measurements[1]
        side2 = measurements[1] * measurements[2]
        side3 = measurements[0] * measurements[2]

        total += (2 * side1) + (2 * side2) + (2 * side3) + min(side1, side2, side3)
    return total
