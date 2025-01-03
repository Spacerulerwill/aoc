from typing import Any


def puzzle(input: str) -> Any:
    lines = [line.strip() for line in input.strip().split("\n")]
    parts = []
    for line in lines:
        split = line.split(":")
        target = int(split[0].strip())
        terms = [int(num) for num in split[1].strip().split()]
        parts.append((target, terms))

    def can_terms_add_to_target(target: int, terms: list[int]) -> bool:
        def backtrack(idx: int, current_value: int) -> bool:
            if idx == len(terms):
                return current_value == target

            if backtrack(idx + 1, current_value + terms[idx]):
                return True

            if backtrack(idx + 1, current_value * terms[idx]):
                return True

            if backtrack(idx + 1, int(str(current_value) + str(terms[idx]))):
                return True

            return False

        return backtrack(1, terms[0]) if terms else target == 0

    sum = 0
    for target, terms in parts:
        if can_terms_add_to_target(target, terms):
            sum += target
    return sum
