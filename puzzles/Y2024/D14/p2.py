import re
from dataclasses import dataclass
from typing import Any


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def puzzle(input: str) -> Any:
    robot_lines = [line.strip() for line in input.strip().split("\n")]
    robots = []
    for line in robot_lines:
        search = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if search is None:
            raise ValueError("Invalid input data")
        robots.append(
            Robot(
                int(search.group(1)),
                int(search.group(2)),
                int(search.group(3)),
                int(search.group(4)),
            )
        )

    WIDTH = 101
    HEIGHT = 103

    def get_image_string(robots: list[Robot]) -> str:
        # Create a set of all robot positions for quick lookup
        positions = set((robot.x, robot.y) for robot in robots)

        # Create the grid as a string
        return "\n".join(
            "".join("+" if (x, y) in positions else "-" for x in range(WIDTH))
            for y in range(HEIGHT)
        )

    def next_frame() -> str:
        for robot in robots:
            robot.x = (robot.x + robot.dx) % WIDTH
            robot.y = (robot.y + robot.dy) % HEIGHT
        x = get_image_string(robots)
        return x

    i = 0
    while "+++++++++++++++++++++++++++++++" not in next_frame():
        i += 1
    return i + 1
