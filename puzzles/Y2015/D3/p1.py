from typing import Any


def puzzle(input: str) -> Any:
    input = input.strip()
    visited_houses = set()
    visited_houses.add((0, 0))
    x, y = (0, 0)
    for char in input:
        match char:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        visited_houses.add((x, y))
    return len(visited_houses)
