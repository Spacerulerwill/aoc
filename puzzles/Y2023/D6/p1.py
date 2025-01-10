import re
from typing import Any

digits = re.compile("([0-9]+)")


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    times = [int(num) for num in re.findall(digits, lines[0])]
    record_distances = [int(num) for num in re.findall(digits, lines[1])]
    num_races = len(times)

    total = 1
    for race_index in range(num_races):
        race_time = times[race_index]
        race_record = record_distances[race_index]
        winning_combinations = 0
        for i in range(race_time + 1):
            distance_travelled = i * (race_time - i)
            if distance_travelled > race_record:
                winning_combinations += 1
        total *= winning_combinations
    return total
