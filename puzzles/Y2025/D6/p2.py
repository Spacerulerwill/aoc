from typing import Any
from math import prod


def puzzle(input: str) -> Any:
    total = 0
    lines = input.splitlines()
    rows = len(lines)
    cols = len(lines[0])
    problems = []
    prev_empty_column = -1

    # all columsn but the last one
    for c in range(cols):
        for r in range(rows):
            if lines[r][c] != " ":
                break
        else:
            # Found empty column
            problem = "\n".join(line[prev_empty_column + 1 : c] for line in lines)
            prev_empty_column = c
            problems.append(problem)
    # last column
    problems.append("\n".join(line[prev_empty_column + 1 :] for line in lines))
    for problem in problems:
        problem_split = problem.splitlines()
        rows = len(problem_split)
        cols = len(problem_split[0])

        numbers = []
        for c in range(cols):
            num = "".join(problem_split[r][c] for r in range(rows - 1))
            numbers.append(int(num))
        print(numbers)
        symbol = problem_split[-1].strip()
        if symbol == "+":
            total += sum(numbers)
        elif symbol == "*":
            total += prod(numbers)
    return total


if __name__ == "__main__":
    print(
        puzzle("""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """)
    )
