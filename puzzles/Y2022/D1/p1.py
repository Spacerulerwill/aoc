from typing import Any


def puzzle(input: str) -> Any:
    groupedCalories = input.strip().split("\n\n")
    highest = 0
    for group in groupedCalories:
        total = sum(int(calorie) for calorie in group.split("\n"))
        if total > highest:
            highest = total
    return highest
