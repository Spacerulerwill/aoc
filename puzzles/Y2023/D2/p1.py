from typing import Any

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    sum_of_ids = 0
    for line in lines:
        split = line.split(": ")
        game_number = int(split[0].replace("Game ", ""))
        rounds = split[1].split(";")
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                cube_split = cube.strip().split(" ")
                color = cube_split[1]
                count = int(cube_split[0])
                match color:
                    case "red":
                        if count > MAX_RED:
                            break
                    case "blue":
                        if count > MAX_BLUE:
                            break
                    case "green":
                        if count > MAX_GREEN:
                            break
            else:
                continue
            break
        else:
            sum_of_ids += game_number
    return sum_of_ids
