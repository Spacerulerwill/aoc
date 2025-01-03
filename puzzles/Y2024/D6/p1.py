from typing import Any


def get_start_pos(grid: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        for c, elem in enumerate(row):
            if elem == "^":
                return r, c
    raise ValueError("Grid has no start position")


def puzzle(input: str) -> Any:
    # convert to grid
    grid = [list(line.strip()) for line in input.strip().split()]
    rows = len(grid)
    cols = len(grid[0])
    # where does guard start
    r, c = get_start_pos(grid)
    # simulation
    visited = 0
    dr, dc = -1, 0
    while r < rows and r >= 0 and c < cols and c >= 0:
        next_r = r + dr
        next_c = c + dc
        if (
            next_r < rows
            and next_r >= 0
            and next_c < cols
            and next_c >= 0
            and grid[next_r][next_c] == "#"
        ):
            dr, dc = dc, -dr
        else:
            if grid[r][c] != "X":
                visited += 1
                grid[r][c] = "X"
            r = next_r
            c = next_c
    return visited
