import re
from typing import Any

pattern = re.compile(r"Card\s+[0-9]+:(.*)\|(.*)")


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    scratchcard_counter = {}
    for idx, line in enumerate(lines):
        if idx not in scratchcard_counter:
            scratchcard_counter[idx] = 1
        search = re.search(pattern, line)
        if search is not None:
            winning_numbers = [int(num) for num in search.group(1).split()]
            our_numbers = [int(num) for num in search.group(2).split()]

            winning_count = sum(
                our_number in winning_numbers for our_number in our_numbers
            )

            for n in range(idx + 1, idx + winning_count + 1):
                scratchcard_counter[n] = (
                    scratchcard_counter.get(n, 1) + scratchcard_counter[idx]
                )
    return sum(scratchcard_counter.values())
