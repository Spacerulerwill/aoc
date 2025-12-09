from typing import Any
from math import prod


def puzzle(input: str) -> Any:
    lines = [line.split() for line in input.splitlines()]

    length = len(lines[0])
    problems = [[lines[j][i] for j in range(5)] for i in range(length)]
    total = 0
    for problem in problems:
        symbol = problem[4]
        if symbol == "+":
            total += sum(int(problem[i]) for i in range(4))
        elif symbol == "*":
            total += prod(int(problem[i]) for i in range(4))
    return total
