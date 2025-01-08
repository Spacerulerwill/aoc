from typing import Any

choice_map = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def puzzle(input: str) -> Any:
    lines = input.strip().split("\n")

    turns = [line.split() for line in lines]
    # rock, paper, scissors
    total_score = 0
    for turn in turns:
        opponent = choice_map[turn[0]]
        us = choice_map[turn[1]]
        if us == 1:
            # we need to lose
            total_score += 1 + (opponent - 2) % 3
        elif us == 2:
            # we need to draw - choose same as them
            total_score += 3 + opponent
        elif us == 3:
            # we need to win the round - choice choice to right-
            total_score += 6 + 1 + (opponent) % 3
    return total_score
