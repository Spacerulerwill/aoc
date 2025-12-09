from typing import Any
from functools import cache


# how many possible paths are there to the end
def puzzle(input: str) -> Any:
    lines = input.splitlines()
    rows = len(lines)
    cols = len(lines[0])

    @cache
    def solve(
        r: int,
        c: int,
    ) -> int:
        if c < 0 or c == cols:
            return 0
        if r == rows:
            return 1
        if lines[r][c] == "^":
            return solve(r + 1, c - 1) + solve(r + 1, c + 1)
        elif lines[r][c] == ".":
            return solve(r + 1, c)
        raise ValueError()

    for c in range(cols):
        if lines[0][c] == "S":
            for r in range(1, rows):
                if lines[r][c] == "^":
                    return solve(r, c)


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
