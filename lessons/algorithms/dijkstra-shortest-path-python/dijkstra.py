"""Dijkstra's shortest-path algorithm using a min-heap priority queue."""

from __future__ import annotations

import heapq
import math


def shortest_path(
    graph: dict,
    start: int,
    destination: int,
) -> tuple[list[int], list[str], float]:
    """Return path nodes, path edge IDs, and total cost.

    The graph must contain non-negative ``lengthMeters`` edge weights.
    """
    adjacency: dict[int, list[dict]] = {node["id"]: [] for node in graph["nodes"]}
    for edge in graph["edges"]:
        if edge["lengthMeters"] < 0:
            raise ValueError("Dijkstra requires non-negative edge weights")
        adjacency[edge["from"]].append(edge)

    if start not in adjacency or destination not in adjacency:
        raise ValueError("start and destination must be graph nodes")

    distance = {start: 0.0}
    previous: dict[int, tuple[int, str]] = {}
    frontier = [(0.0, start)]
    settled: set[int] = set()

    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)
        if node == destination:
            break

        for edge in adjacency[node]:
            candidate = cost + edge["lengthMeters"]
            if candidate < distance.get(edge["to"], math.inf):
                distance[edge["to"]] = candidate
                previous[edge["to"]] = (node, edge["edgeId"])
                heapq.heappush(frontier, (candidate, edge["to"]))

    if destination not in settled:
        raise ValueError("destination is unreachable")

    nodes = [destination]
    edges: list[str] = []
    while nodes[-1] != start:
        parent, edge_id = previous[nodes[-1]]
        nodes.append(parent)
        edges.append(edge_id)
    return list(reversed(nodes)), list(reversed(edges)), distance[destination]


if __name__ == "__main__":
    example = {
        "nodes": [{"id": value} for value in range(4)],
        "edges": [
            {"edgeId": "direct", "from": 0, "to": 3, "lengthMeters": 10},
            {"edgeId": "a", "from": 0, "to": 1, "lengthMeters": 2},
            {"edgeId": "b", "from": 1, "to": 2, "lengthMeters": 2},
            {"edgeId": "c", "from": 2, "to": 3, "lengthMeters": 2},
        ],
    }
    print(shortest_path(example, 0, 3))
