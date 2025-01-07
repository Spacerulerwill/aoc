from typing import Any
from collections import defaultdict
from functools import cmp_to_key


def puzzle(input: str) -> Any:
    s = input.split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in s[0].strip().splitlines()]
    updates = [
        list(map(int, update.split(","))) for update in s[1].strip().splitlines()
    ]

    # map of every number to the set of every number it must come before
    before = defaultdict(set)
    for rule in rules:
        before[rule[0]].add(rule[1])

    def compare(a: int, b: int) -> int:
        if b in before[a]:
            return -1
        return 0

    sum = 0
    for update in updates:
        seen: set[int] = set()
        for num in update:
            if len(seen.intersection(before[num])) != 0:
                update.sort(key=cmp_to_key(compare))
                sum += update[len(update) // 2]
                break
            seen.add(num)
    return sum
