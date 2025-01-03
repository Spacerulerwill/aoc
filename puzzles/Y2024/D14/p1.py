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

    top_left_quadrant = 0
    top_right_quadrant = 0
    bottom_left_quadrant = 0
    bottom_right_quadrant = 0

    WIDTH = 101
    HEIGHT = 103
    MIDDLE_X = WIDTH // 2
    MIDDLE_Y = HEIGHT // 2

    for robot in robots:
        robot.x = (robot.x + robot.dx * 100) % WIDTH
        robot.y = (robot.y + robot.dy * 100) % HEIGHT

    for robot in robots:
        # Determine the quadrant
        if robot.x < MIDDLE_X and robot.y < MIDDLE_Y:
            top_left_quadrant += 1
        elif robot.x > MIDDLE_X and robot.y < MIDDLE_Y:
            top_right_quadrant += 1
        elif robot.x < MIDDLE_X and robot.y > MIDDLE_Y:
            bottom_left_quadrant += 1
        elif robot.x > MIDDLE_X and robot.y > MIDDLE_Y:
            bottom_right_quadrant += 1

    return (
        top_left_quadrant
        * top_right_quadrant
        * bottom_right_quadrant
        * bottom_left_quadrant
    )
