import re
from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    valid_passwords = 0
    for line in lines:
        if match := re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line):
            min = int(match.group(1))
            max = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)

            if password.count(letter) in range(min, max + 1):
                valid_passwords += 1
    return valid_passwords
