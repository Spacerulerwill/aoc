import hashlib
from typing import Any


def puzzle(input: str) -> Any:
    input = input.strip()
    i = 0
    while True:
        hash_hex_string = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hash_hex_string[:6] == "000000":
            return i
        i += 1
