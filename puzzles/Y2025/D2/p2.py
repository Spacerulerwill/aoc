from typing import Any


def is_id_invalid(number: str) -> bool:
    if len(number) < 2:
        return False
    for i in range(1, (len(number) // 2) + 1):
        if len(number) % i != 0:
            continue
        times = len(number) // i
        substring = number[:i]
        if substring * times == number:
            return True
    return False


def puzzle(input: str) -> Any:
    _sum = 0
    ranges = [
        [start, end] for part in input.split(",") for start, end in [part.split("-")]
    ]
    for start, end in ranges:
        for i in range(int(start), int(end) + 1):
            if is_id_invalid(str(i)):
                _sum += i
    return _sum
