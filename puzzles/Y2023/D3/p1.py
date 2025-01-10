from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    coords = set()
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for dy in range(y - 1, y + 2):
                for dx in range(x - 1, x + 2):
                    if (
                        dy < 0
                        or dy >= len(lines)
                        or dx < 0
                        or dx >= len(lines[dy])
                        or not lines[dy][dx].isdigit()
                    ):
                        continue
                    while dx > 0 and lines[dy][dx - 1].isdigit():
                        dx -= 1
                    coords.add((dy, dx))

    numbers = []
    for y, x in coords:
        number_string = ""
        while x < len(lines[y]) and lines[y][x].isdigit():
            number_string += lines[y][x]
            x += 1
        numbers.append(int(number_string))
    return sum(numbers)
