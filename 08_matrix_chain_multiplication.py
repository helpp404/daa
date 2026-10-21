"""
EXPERIMENT 8: MATRIX CHAIN MULTIPLICATION (DYNAMIC PROGRAMMING)
THEORY: Multiplying matrices in different orders requires different
numbers of scalar multiplications. DP finds the CHEAPEST ORDER.
Note: this finds the order, it does not calculate a matrix product.

ALGORITHM (simple English):
1. Multiplying one matrix has cost 0.
2. Consider each possible chain length from 2 to n.
3. For each chain, try every possible splitting position k.
4. Add (left cost) + (right cost) + (cost to join two results).
5. Save the smallest value and its split position in tables.

TIME COMPLEXITY (n = number of matrices):
Best: O(n^3) -- Every chain and every split are checked regardless of sizes.
Worst: O(n^3) -- Same three nested loops for all inputs.
Space: O(n^2) -- Cost table and split table.

VIVA:
Q1. Does it multiply actual matrices? A. No, just finds best order.
Q2. Why DP? A. Costs of smaller subchains are reused.
Q3. Base case? A. One matrix has multiplication cost 0.
"""


def matrix_chain_order(dimensions):
    # Dimensions [10, 20, 30] means two matrices: 10x20, 20x30.
    n = len(dimensions) - 1
    if n <= 0:
        return 0, []
    cost = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            for k in range(i, j):
                current = (cost[i][k] + cost[k + 1][j]
                           + dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                if current < cost[i][j]:
                    cost[i][j] = current
                    split[i][j] = k
    return cost[0][n - 1], split


def show_order(split, i, j):
    if i == j:
        return f'A{i + 1}'
    k = split[i][j]
    return f'({show_order(split, i, k)} x {show_order(split, k + 1, j)})'


if __name__ == '__main__':
    dimensions = [10, 30, 5, 60]  # A1=10x30, A2=30x5, A3=5x60.
    answer, splits = matrix_chain_order(dimensions)
    print('Minimum scalar multiplications:', answer)
    print('Best order:', show_order(splits, 0, len(dimensions) - 2))
