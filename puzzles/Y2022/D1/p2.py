import heapq
from typing import Any


def puzzle(input: str) -> Any:
    groupedCalories = input.strip().split("\n\n")
    elvesCalories = []
    for group in groupedCalories:
        elvesCalories.append(sum(int(calorie) for calorie in group.split("\n")))
    # convert to negative to get 3 smallest using min heap
    elvesCalories = [-calories for calories in elvesCalories]
    heapq.heapify(elvesCalories)
    return sum(heapq.heappop(elvesCalories) * -1 for _ in range(3))
