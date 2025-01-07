from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    nice_strings = 0
    for line in lines:
        first = False
        for i in range(len(line) - 3):
            sub = line[i:i + 2]
            if sub in line[i + 2:]:
                first = True
                break
        if not first:
            continue
        second = False
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                second = True
                break
        if second:
            nice_strings += 1
    return nice_strings
