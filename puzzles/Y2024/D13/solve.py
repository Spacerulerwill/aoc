import re
from typing import Optional
from dataclasses import dataclass


@dataclass
class Game:
    da: tuple[int, int]
    db: tuple[int, int]
    target: tuple[int, int]


def parse_games(input: str, addend: int = 0) -> list[Game]:
    games = []
    matches = re.findall(
        r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""",
        input,
    )
    for match in matches:
        games.append(
            Game(
                (int(match[0]), int(match[1])),
                (int(match[2]), int(match[3])),
                (int(match[4]) + addend, int(match[5]) + addend),
            )
        )
    print(len(games))
    return games


def get_tokens_for_win(game: Game) -> Optional[int]:
    ax, ay = game.da
    bx, by = game.db
    target_x, target_y = game.target
    # solve linear equation:
    # (ax)a + (bx)b = target_x
    # (ay)a + (by)b = target_y
    # using matrices
    # | ax, bx | | a | = | target_x |
    # | ay, by | | b | = | target_y |
    # find inverse
    determinant = ax * by - bx * ay
    inverse_matrix = [
        [by / determinant, -bx / determinant],
        [-ay / determinant, ax / determinant],
    ]

    # multiply the inverse matrix by target matrix to get result
    a = inverse_matrix[0][0] * target_x + inverse_matrix[0][1] * target_y
    b = inverse_matrix[1][0] * target_x + inverse_matrix[1][1] * target_y

    int_a = int(round(a))
    int_b = int(round(b))
    if int_a * ax + int_b * bx == target_x and int_a * ay + int_b * by == target_y:
        return int_a * 3 + int_b
    else:
        return None


def solve(input: str, addend: int = 0) -> int:
    return sum(get_tokens_for_win(game) or 0 for game in parse_games(input, addend))
