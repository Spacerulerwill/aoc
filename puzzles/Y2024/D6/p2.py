from typing import Any


def get_start_pos(grid: list[list[str]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        for c, elem in enumerate(row):
            if elem == "^":
                return r, c
    raise ValueError("Grid has no start position")


# Same as part 1, except it records the positions visited
def part_1(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    r, c = get_start_pos(grid)
    visited = []
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
                visited.append((r, c))
                grid[r][c] = "X"
            r = next_r
            c = next_c
    return visited


def try_find_cycle(grid: list[list[str]], start: tuple[int, int]) -> bool:
    start_r, start_c = start
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    r, c = start_r, start_c
    dr, dc = -1, 0
    while 0 <= r < rows and 0 <= c < cols:
        state = (r, c, dr, dc)
        if state in visited:
            return True
        visited.add(state)
        next_r, next_c = r + dr, c + dc
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == "#":
            dr, dc = dc, -dr
        else:
            r, c = next_r, next_c
    return False


def puzzle(input: str) -> Any:
    grid = [list(line.strip()) for line in input.strip().split()]
    found = 0
    start_r, start_c = get_start_pos(grid)
    # we only need to check the squares on the path from part 1
    path_positions = part_1(grid)
    for r, c in path_positions:
        if grid[r][c] in {"#", "^"}:
            continue
        prev = grid[r][c]
        grid[r][c] = "#"
        if try_find_cycle(grid, (start_r, start_c)):
            found += 1
        grid[r][c] = prev
    return found
