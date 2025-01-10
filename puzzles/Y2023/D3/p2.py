from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    total_gear_ratio = 0
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch != "*":
                continue
            coordinate_pairs = set()
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
                    coordinate_pairs.add((dy, dx))
            if len(coordinate_pairs) != 2:
                continue
            ns = []
            for dy, dx in coordinate_pairs:
                s = ""
                while dx < len(lines[dy]) and lines[dy][dx].isdigit():
                    s += lines[dy][dx]
                    dx += 1
                ns.append(int(s))
            gear_ratio = ns[0] * ns[1]
            total_gear_ratio += gear_ratio
    return total_gear_ratio
