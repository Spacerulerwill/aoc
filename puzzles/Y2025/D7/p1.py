from typing import Any


def puzzle(input: str) -> Any:
    lines = input.splitlines()
    rows = len(lines)
    cols = len(lines[0])
    tachyons = set()
    for c in range(cols):
        if lines[0][c] == "S":
            tachyons.add(c)
            break
    else:
        raise ValueError("No starting tachyon")
    total = 0
    for r in range(1, rows):
        for c in range(cols):
            if lines[r][c] == "^" and c in tachyons:
                tachyons.remove(c)
                total += 1
                if c > 0:
                    tachyons.add(c - 1)
                if c < cols - 1:
                    tachyons.add(c + 1)
    return total


if __name__ == "__main__":
    print(
        puzzle(""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""")
    )
