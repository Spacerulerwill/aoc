from typing import Any


STR_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    sum = 0
    for line in lines:
        digits = []
        for idx, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))
            for d, val in enumerate(STR_DIGITS):
                if line[idx:].startswith(val):
                    digits.append(d + 1)
        sum += (digits[0] * 10) + digits[-1]
    return sum
