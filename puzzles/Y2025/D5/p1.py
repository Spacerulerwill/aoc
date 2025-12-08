from typing import Any


# naive approach
def puzzle(input: str) -> Any:
    fresh = 0
    split = input.split("\n\n")
    ranges_string = split[0]
    ingredient_ids_string = split[1]

    ranges = [tuple(map(int, line.split("-"))) for line in ranges_string.splitlines()]
    ingredient_ids = [int(id) for id in ingredient_ids_string.splitlines()]

    for id in ingredient_ids:
        for low, high in ranges:
            if low <= id <= high:
                fresh += 1
                break
    return fresh
