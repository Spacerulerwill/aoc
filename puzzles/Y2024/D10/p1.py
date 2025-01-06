from typing import Any


def find_trailhead_score(grid: list[list[int]], r: int, c: int) -> int:
    score = 0
    nines_found = set()
    rows = len(grid)
    cols = len(grid[0])

    def backtrack(r: int, c: int) -> None:
        nonlocal score
        if grid[r][c] == 9:
            if (r, c) not in nines_found:
                nines_found.add((r, c))
                score += 1
            return

        # Check all 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r = r + dr
            new_c = c + dc
            if (
                0 <= new_r < rows
                and 0 <= new_c < cols
                and grid[new_r][new_c] == grid[r][c] + 1
            ):
                backtrack(new_r, new_c)

    backtrack(r, c)
    return score


def puzzle(input: str) -> Any:
    grid = [
        [int(num) if num != "." else -55 for num in line.strip()]
        for line in input.strip().split("\n")
    ]

    rows = len(grid)
    cols = len(grid[0])

    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_score += find_trailhead_score(grid, r, c)

    return total_score
