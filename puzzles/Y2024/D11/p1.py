from typing import Any
from .blink import blink_stones


def puzzle(input: str) -> Any:
    return blink_stones((int(num) for num in input.strip().split()), 25)
