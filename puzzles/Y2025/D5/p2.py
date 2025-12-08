from typing import Any


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(intervals) <= 1:
        return intervals
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    for i in range(1, len(sorted_intervals)):
        prev_low, prev_high = merged[-1]
        current_low, current_high = sorted_intervals[i]
        if prev_high < current_low:
            merged.append((current_low, current_high))
        else:
            # merge intervals
            new_interval = (prev_low, max(prev_high, current_high))
            merged[-1] = new_interval
    return merged


# naive approach
def puzzle(input: str) -> Any:
    split = input.split("\n\n")
    intervals_string = split[0]

    intervals = [
        (int(a), int(b))
        for line in intervals_string.splitlines()
        for a, b in [line.split("-")]
    ]

    merged_intervals = merge_intervals(intervals)
    return sum(interval[1] - interval[0] + 1 for interval in merged_intervals)
