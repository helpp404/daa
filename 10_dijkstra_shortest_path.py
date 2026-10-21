"""
EXPERIMENT 10: DIJKSTRA'S SINGLE-SOURCE SHORTEST PATH
THEORY: Find minimum distances from ONE starting vertex to every other
reachable vertex. Edges must have NONNEGATIVE weights.
This easy practical version uses an adjacency matrix.

ALGORITHM (simple English):
1. Set source distance to 0; other distances to infinity.
2. Select unvisited vertex with smallest current distance.
3. Mark it visited; its distance is now final.
4. Check its neighbors: if path through it is shorter, update distance.
5. Repeat until no reachable unvisited vertices remain.

TIME COMPLEXITY (V = vertices):
Best: O(V^2) -- Matrix-based minimum search/neighbors require scans.
Worst: O(V^2) -- Scans are done regardless of edge weights.
Space: O(V) EXTRA for distances/visited; matrix INPUT takes O(V^2).

VIVA:
Q1. Can we use negative edges? A. No, Dijkstra assumes nonnegative weights.
Q2. What is relaxation? A. Shortening a tentative distance via an edge.
Q3. BFS vs Dijkstra? A. BFS for unweighted; Dijkstra for weighted graphs.
"""


def dijkstra(graph, source):
    # graph[u][v] = weight; None if edge does not exist.
    n = len(graph)
    distance = [float('inf')] * n
    visited = [False] * n
    distance[source] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or distance[i] < distance[u]):
                u = i  # Nearest not-yet-visited vertex.
        if u == -1 or distance[u] == float('inf'):
            break  # All remaining vertices are unreachable.

        visited[u] = True
        for v in range(n):
            weight = graph[u][v]
            if weight is not None and not visited[v]:
                possible = distance[u] + weight
                if possible < distance[v]:
                    distance[v] = possible
    return distance


if __name__ == '__main__':
    graph = [
        [0, 4, 1, None],
        [4, 0, 2, 1],
        [1, 2, 0, 5],
        [None, 1, 5, 0],
    ]
    print('Shortest distances from vertex 0:', dijkstra(graph, 0))
