from typing import Any
from collections import deque


def bfs_grid(
    grid: list[list[str]], visited: list[list[bool]], r: int, c: int
) -> tuple[int, int]:
    """traverse the grid marking of all characters as seen, return the area and perimeters"""
    rows = len(grid)
    cols = len(grid[0])
    region_char = grid[r][c]
    area = 0
    perimeter = 0
    queue = deque([(r, c)])
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            r, c = queue.popleft()
            # check its in bounds, not already visited and the same character
            if (
                0 <= r < rows
                and 0 <= c < cols
                and not visited[r][c]
                and grid[r][c] == region_char
            ):
                area += 1
                visited[r][c] = True
                # check to see if its a perimeter coordinate
                if r == rows - 1 or grid[r + 1][c] != region_char:
                    perimeter += 1
                if r == 0 or grid[r - 1][c] != region_char:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] != region_char:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] != region_char:
                    perimeter += 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((r + dr, c + dc))
    return area, perimeter


def puzzle(input: str) -> Any:
    grid = [list(line.strip()) for line in input.strip().split()]
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    price = 0
    for r in range(rows):
        for c in range(cols):
            # visited already
            if visited[r][c]:
                continue
            area, perimeter = bfs_grid(grid, visited, r, c)
            price += area * perimeter
    return price
