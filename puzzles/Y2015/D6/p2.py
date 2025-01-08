import re
from typing import Any


def turn_on(current: int) -> int:
    return current + 1


def turn_off(current: int) -> int:
    return max(current - 1, 0)


def flip(current: int) -> int:
    return current + 2


def puzzle(input: str) -> Any:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    lines = [line.strip() for line in input.strip().splitlines()]
    for line in lines:
        for regex, function in [
            (r"turn on (\d+),(\d+) through (\d+),(\d+)", turn_on),
            (r"turn off (\d+),(\d+) through (\d+),(\d+)", turn_off),
            (r"toggle (\d+),(\d+) through (\d+),(\d+)", flip),
        ]:
            match = re.match(regex, line)
            if match:
                x0, y0 = int(match.group(1)), int(match.group(2))
                x1, y1 = int(match.group(3)), int(match.group(4))

                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        lights[y][x] = function(lights[y][x])
                break
    return sum(sum(row) for row in lights)
