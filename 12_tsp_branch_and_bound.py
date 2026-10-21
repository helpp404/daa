"""
EXPERIMENT 12: TRAVELLING SALESMAN PROBLEM (BRANCH AND BOUND)
THEORY: Find the shortest tour that visits EVERY city exactly once and
returns to the starting city. TSP is NP-hard.
Branch = try next city. Bound = optimistic estimate of route cost.
Prune = skip any partial route that cannot beat the best known tour.

ALGORITHM (simple English):
1. Start tour from city 0. Precompute cheapest outgoing edge per city.
2. Try each unvisited city as next stop (branch).
3. Estimate minimum possible full-tour cost (lower bound).
4. If estimate >= best complete tour so far, skip this partial route.
5. Otherwise recursively visit another city.
6. After every city is visited, add cost of return to 0; update best.

TIME COMPLEXITY (n = number of cities):
Best: O(n^2) in a highly favorable case with very early pruning,
      including scanning the n x n cost matrix for preprocessing.
Worst: O(n!) -- The algorithm may need to explore almost all tours.
Reason: Bounds prune some tours, but no guarantee they prune many.
Space: O(n^2) for input matrix; O(n) additional for recursion/path/visited.

VIVA:
Q1. Branch and Bound vs brute force? A. It prunes unpromising tours.
Q2. What is a lower bound? A. A safe underestimate of remaining cost.
Q3. TSP vs shortest path? A. TSP visits every city and returns home.
"""


def tsp_branch_and_bound(dist):
    n = len(dist)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0, 0]

    # Assumes complete graph with nonnegative distances.
    min_out = [min(dist[i][j] for j in range(n) if j != i)
               for i in range(n)]
    visited = [False] * n
    visited[0] = True
    best_cost, best_path = float('inf'), []

    def search(city, count, cost, remaining_min, path):
        nonlocal best_cost, best_path
        if count == n:
            total = cost + dist[city][0]  # Return home.
            if total < best_cost:
                best_cost = total
                best_path = path + [0]
            return

        # Current city and all unvisited cities must each have an outgoing
        # edge in final tour. Their min outgoing costs are a LOWER bound.
        bound = cost + min_out[city] + remaining_min
        if bound >= best_cost:
            return

        for nxt in range(1, n):
            if not visited[nxt]:
                new_cost = cost + dist[city][nxt]
                if new_cost >= best_cost:  # Nonnegative distances.
                    continue
                visited[nxt] = True
                search(nxt, count + 1, new_cost,
                       remaining_min - min_out[nxt], path + [nxt])
                visited[nxt] = False

    search(0, 1, 0, sum(min_out[1:]), [0])
    return best_cost, best_path


if __name__ == '__main__':
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    best, path = tsp_branch_and_bound(distances)
    print('Minimum tour cost:', best)
    print('Best route:', ' -> '.join(map(str, path)))
