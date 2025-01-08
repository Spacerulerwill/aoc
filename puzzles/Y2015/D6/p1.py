import re
from typing import Any


def turn_on(current: bool) -> bool:
    return True


def turn_off(current: bool) -> bool:
    return False


def toggle(current: bool) -> bool:
    return not current


def puzzle(input: str) -> Any:
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    lines = [line.strip() for line in input.strip().splitlines()]
    for line in lines:
        for regex, function in [
            (r"turn on (\d+),(\d+) through (\d+),(\d+)", turn_on),
            (r"turn off (\d+),(\d+) through (\d+),(\d+)", turn_off),
            (r"toggle (\d+),(\d+) through (\d+),(\d+)", toggle),
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
