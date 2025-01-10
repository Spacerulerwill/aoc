from typing import Any

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    sum_of_powers = 0
    for line in lines:
        split = line.split(": ")
        rounds = split[1].split(";")

        max_red = 0
        max_green = 0
        max_blue = 0

        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                cube_split = cube.strip().split(" ")
                color = cube_split[1]
                count = int(cube_split[0])
                match color:
                    case "red":
                        if count > max_red:
                            max_red = count
                    case "blue":
                        if count > max_blue:
                            max_blue = count
                    case "green":
                        if count > max_green:
                            max_green = count

        sum_of_powers += max_blue * max_green * max_red
    return sum_of_powers
