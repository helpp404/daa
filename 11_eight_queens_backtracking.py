# EXPERIMENT 11: 8-QUEENS PROBLEM USING BACKTRACKING
#
# THEORY (simple):
# Place 8 queens on an 8x8 chessboard so that no two queens attack
# each other. Queens attack along rows, columns, and diagonals.
# Backtracking means: try a position; if it makes a future solution
# impossible, undo that choice and try another position.
#
# ALGORITHM (say these steps in the viva):
# 1. Start with the first row.
# 2. Try placing a queen in each column of that row.
# 3. A position is safe if its column and two diagonals are unused.
# 4. If safe, place the queen and move to the next row recursively.
# 5. If the next rows cannot be completed, remove the queen (backtrack).
# 6. When all 8 rows have queens, print the solution.
#
# TIME COMPLEXITY (for N queens; here N = 8):
# Best: O(N) for finding the first solution when the first attempted
#       column in each row leads straight to success: N placements.
# Worst: O(N!) for this backtracking approach (common upper bound).
#        In the worst case, many possible column arrangements must
#        be tried before a solution is found or search finishes.
# NOTE: These bounds describe the first-solution search below,
#       not a program that prints EVERY possible solution.
# SPACE: O(N) auxiliary space for recursion and sets; the displayed
#        board uses O(N^2) space.
#
# IMPORTANT VIVA QUESTIONS:
# Q1. What is backtracking?
# A. Try a choice, recursively continue, and undo it if it fails.
# Q2. Why do we check diagonals as well as columns?
# A. A queen can attack vertically and diagonally (rows are already unique).
# Q3. Difference between backtracking and brute force?
# A. Backtracking stops exploring a partial arrangement as soon as
#    it breaks a constraint; brute force can test complete arrangements.
#
# INPUT: Change n = 8 at the bottom. For the actual 8-Queens practical,
#        keep n = 8. No keyboard input is required.


def solve_n_queens(n):
    columns = set()       # columns that already contain a queen
    diag1 = set()         # row - col identifies one diagonal direction
    diag2 = set()         # row + col identifies the other direction
    positions = []        # positions[row] = queen's column in that row

    def backtrack(row):
        if row == n:     # all rows filled: a valid solution was found
            return True

        for col in range(n):
            if col in columns or row - col in diag1 or row + col in diag2:
                continue  # queen would be attacked, so try next column

            # Place queen
            positions.append(col)
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True  # stop after the FIRST valid solution

            # Undo this choice because it didn't lead to a solution
            positions.pop()
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False  # no column worked in this row

    return positions if backtrack(0) else None


def print_board(positions, n):
    for row in range(n):
        print(' '.join('Q' if col == positions[row] else '.' for col in range(n)))


if __name__ == '__main__':
    n = 8  # Change this for N-Queens; keep 8 for your practical
    solution = solve_n_queens(n)
    if solution is None:
        print('No solution exists.')
    else:
        print(f'{n}-Queens solution (Q = queen, . = empty):')
        print_board(solution, n)
