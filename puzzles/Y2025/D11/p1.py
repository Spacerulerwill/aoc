from typing import Any


def puzzle(input: str) -> Any:
    # create adjancency list
    adjacency_list = {}
    lines = input.splitlines()
    for line in lines:
        line_split = line.split(":")
        first = line_split[0]
        connections = line_split[1].split()
        adjacency_list[first] = connections

    visited = set()
    paths = 0

    def dfs(node: str) -> None:
        nonlocal paths
        if node == "out":
            paths += 1
            return
        connections = adjacency_list[node]
        visited.add(node)
        for connection in connections:
            if connection not in visited:
                dfs(connection)
        visited.remove(node)

    dfs("you")
    return paths
