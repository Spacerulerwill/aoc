from typing import Any
from functools import cache


def puzzle(input: str) -> Any:
    # create adjancency list
    adjacency_list = {}
    lines = input.splitlines()
    for line in lines:
        line_split = line.split(":")
        first = line_split[0]
        connections = line_split[1].split()
        adjacency_list[first] = connections
    adjacency_list["out"] = []

    @cache
    def number_of_paths(
        node: str, goal: str, fft: bool = False, dac: bool = False
    ) -> int:
        if node == goal and fft and dac:
            return 1
        total = 0
        for next in adjacency_list[node]:
            total += number_of_paths(
                next, goal, fft or node == "fft", dac or node == "dac"
            )
        return total

    return number_of_paths("svr", "out")
