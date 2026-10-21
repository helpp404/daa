"""
EXPERIMENT 15: APPROXIMATION ALGORITHM FOR VERTEX COVER
THEORY: A vertex cover is a set of vertices touching EVERY edge.
Minimum Vertex Cover is NP-hard, so an approximation gives a quick
valid answer that may not be minimum. This method is a 2-approximation:
chosen cover is at most twice as large as the minimum cover.

ALGORITHM (simple English):
1. Start with empty 'cover' set.
2. Check every edge (u, v).
3. If neither endpoint is already in cover, add BOTH u and v.
4. Continue until all edges have been checked.
5. Return chosen vertices; every edge is covered by at least one.

TIME COMPLEXITY (V = vertices, E = edges):
Best: O(E) -- A single scan of all E edges.
Worst: O(E) -- Same scan, using average O(1) set lookups.
Space: O(V) -- Stores at most V vertices in the cover.

VIVA:
Q1. Vertex cover? A. A set touching at least one endpoint of each edge.
Q2. Why 2-approximation? A. Cover size <= 2 times optimal cover size.
Q3. Is answer always minimum? A. No, minimum vertex cover is NP-hard.
"""


def approximate_vertex_cover(edges):
    cover = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            # Uncovered edge: choose both endpoints.
            cover.add(u)
            cover.add(v)
    return cover


if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    cover = approximate_vertex_cover(edges)
    print('Edges:', edges)
    print('Approximate vertex cover:', sorted(cover))
    print('All edges covered?', all(u in cover or v in cover for u, v in edges))
