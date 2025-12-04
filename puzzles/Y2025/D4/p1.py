from typing import Any


def puzzle(input: str) -> Any:
    rolls = 0
    grid = [list(line) for line in input.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    def is_roll(r: int, c: int) -> bool:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        return grid[r][c] == "@"

    def has_fewer_than_four_neighbours(r: int, c: int) -> bool:
        surrounding = 0
        for dr, dc in {
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
        }:
            if is_roll(r + dr, c + dc):
                surrounding += 1
            if surrounding == 4:
                return False
        return True

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "@":
                if has_fewer_than_four_neighbours(r, c):
                    rolls += 1
    return rolls


if __name__ == "__main__":
    print(
        puzzle("""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""")
    )
