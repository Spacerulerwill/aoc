from typing import Any


def puzzle(input: str) -> Any:
    input = input.strip()
    visited_houses = set()
    visited_houses.add((0, 0))
    santa_x, santa_y = (0, 0)
    robot_santa_x, robot_santa_y = (0, 0)
    for i in range(0, len(input), 2):
        match input[i]:
            case "^":
                santa_y += 1
            case "v":
                santa_y -= 1
            case ">":
                santa_x += 1
            case "<":
                santa_x -= 1
        visited_houses.add((santa_x, santa_y))
        match input[i + 1]:
            case "^":
                robot_santa_y += 1
            case "v":
                robot_santa_y -= 1
            case ">":
                robot_santa_x += 1
            case "<":
                robot_santa_x -= 1
        visited_houses.add((robot_santa_x, robot_santa_y))
    return len(visited_houses)
