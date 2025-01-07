from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    nice_strings = 0
    for line in lines:
        vowel_count = 0
        for char in line:
            if char in "aeiou":
                vowel_count += 1
        if vowel_count < 3:
            continue

        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                break
        else:
            continue

        if any(substring in line for substring in ["ab", "cd", "pq", "xy"]):
            continue
        nice_strings += 1
    return nice_strings
