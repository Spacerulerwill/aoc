import re
from typing import Any

pattern = re.compile(r"Card\s+[0-9]+:(.*)\|(.*)")


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.splitlines()]
    total_points = 0
    for line in lines:
        search = re.search(pattern, line)
        if search is not None:
            winning_number_count = 0
            winning_numbers = [int(num) for num in search.group(1).split()]
            our_numbers = [int(num) for num in search.group(2).split()]

            for number in winning_numbers:
                if number in our_numbers:
                    winning_number_count += 1

            if winning_number_count != 0:
                scratch_card_value = 2 ** (winning_number_count - 1)
                total_points += scratch_card_value
    return total_points
