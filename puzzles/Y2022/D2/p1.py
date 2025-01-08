from typing import Any

choice_map = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def puzzle(input: str) -> Any:
    lines = input.strip().split("\n")
    turns = [line.split() for line in lines]

    def score_for_round(opponent: str, us: str) -> int:
        score = 0
        us_int = choice_map[us]
        opponent_int = choice_map[opponent]
        # always add our choice
        score += us_int
        # draw?
        if opponent_int == us_int:
            score += 3
        # did we win? we always win if our choice is after theirs in order rock, paper, scissors
        elif 1 + (us_int - 2) % 3 == opponent_int:
            score += 6
        return score

    total_score = 0
    for turn in turns:
        total_score += score_for_round(turn[0], turn[1])
    return total_score
