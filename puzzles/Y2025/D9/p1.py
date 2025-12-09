from typing import Any
from itertools import combinations


def puzzle(input: str) -> Any:
    def calculate_rectangle_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
        dx = abs(p1[0] - p2[0]) + 1
        dy = abs(p1[1] - p2[1]) + 1
        return dx * dy

    pairs = [tuple(int(num) for num in pair.split(",")) for pair in input.splitlines()]
    return max(
        calculate_rectangle_area((c[0][0], c[0][1]), (c[1][0], c[1][1]))
        for c in combinations(pairs, 2)
    )


if __name__ == "__main__":
    print(
        puzzle("""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""")
    )
