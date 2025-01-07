from typing import Any
from math import prod


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.strip().split("\n")]
    total = 0
    for line in lines:
        measurements = [int(measurement) for measurement in line.split("x")]
        total += prod(measurements)
        measurements.remove(max(measurements))
        total += 2 * measurements[0] + 2 * measurements[1]
    return total
