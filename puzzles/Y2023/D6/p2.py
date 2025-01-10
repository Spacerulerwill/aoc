import re
from typing import Any

digits = re.compile("([0-9]+)")


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    time = int("".join(num for num in re.findall(digits, lines[0])))
    record_distance = int("".join(num for num in re.findall(digits, lines[1])))

    # iterate from start to find first value of i that wins a race
    first = 0
    for i in range(time + 1):
        distance_travelled = i * (time - i)
        if distance_travelled > record_distance:
            first = i
            break

    # iterate from the end to find the last value of i that wins a race
    last = 0
    for i in range(time + 1, -1, -1):
        distance_travelled = i * (time - i)
        if distance_travelled > record_distance:
            last = i
            break
    return last - first + 1
