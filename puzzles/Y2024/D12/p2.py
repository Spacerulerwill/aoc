from typing import Any
from collections import deque


def bfs_grid(
    grid: list[list[str]], visited: list[list[bool]], start_r: int, start_c: int
) -> tuple[int, int]:
    """Traverse the grid marking off all characters as seen, return the area and amount of corners (same as sides)"""
    rows = len(grid)
    cols = len(grid[0])
    region_char = grid[start_r][start_c]
    # BFS to find area
    area = 0
    queue = deque([(start_r, start_c)])

    def is_present(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == region_char

    all = []
    corners = 0
    while queue:
        r, c = queue.popleft()
        # Check it's in bounds, not already visited, and the same character
        if (
            0 <= r < rows
            and 0 <= c < cols
            and not visited[r][c]
            and grid[r][c] == region_char
        ):
            area += 1
            visited[r][c] = True
            if r == rows - 1 or grid[r + 1][c] != region_char:
                all.append((r, c))
            if r == 0 or grid[r - 1][c] != region_char:
                all.append((r, c))
            if c == cols - 1 or grid[r][c + 1] != region_char:
                all.append((r, c))
            if c == 0 or grid[r][c - 1] != region_char:
                all.append((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                queue.append((r + dr, c + dc))

            # fuck
            if (
                (is_present(r, c - 1) and is_present(r - 1, c))
                and not is_present(r - 1, c - 1)
            ) or (not is_present(r, c - 1) and not is_present(r - 1, c)):
                corners += 1
            if (
                (is_present(r, c + 1) and is_present(r - 1, c))
                and not is_present(r - 1, c + 1)
            ) or (not is_present(r, c + 1) and not is_present(r - 1, c)):
                corners += 1
            if (
                (is_present(r, c - 1) and is_present(r + 1, c))
                and not is_present(r + 1, c - 1)
            ) or (not is_present(r, c - 1) and not is_present(r + 1, c)):
                corners += 1
            if (
                (is_present(r, c + 1) and is_present(r + 1, c))
                and not is_present(r + 1, c + 1)
            ) or (not is_present(r, c + 1) and not is_present(r + 1, c)):
                corners += 1

    return area, corners


def puzzle(input: str) -> Any:
    grid = [list(line.strip()) for line in input.strip().split()]
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    price = 0
    for r in range(rows):
        for c in range(cols):
            # Visited already
            if visited[r][c]:
                continue
            area, sides = bfs_grid(grid, visited, r, c)
            price += area * sides
    return price
