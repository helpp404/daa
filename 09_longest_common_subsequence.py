"""
EXPERIMENT 9: LONGEST COMMON SUBSEQUENCE (DYNAMIC PROGRAMMING)
THEORY: A subsequence maintains ORDER but may SKIP characters.
Find the longest character sequence present in both given strings.

ALGORITHM (simple English):
1. Make DP table with one extra row and column of zeros.
2. If last characters match: add 1 to diagonal DP value.
3. If they do not match: take max of top or left DP value.
4. Last cell contains LCS length; trace back for one actual LCS.

TIME COMPLEXITY (n and m = the two string lengths):
Best: O(n*m) -- DP fills every table cell even if strings are identical.
Worst: O(n*m) -- DP also fills every cell if strings are unrelated.
Space: O(n*m) -- Full table is stored to reconstruct the sequence.

VIVA:
Q1. Substring vs subsequence? A. Substring continuous; subsequence may skip.
Q2. Base case? A. If one string is empty, LCS length is 0.
Q3. Why DP? A. Results for smaller pairs of prefixes are reused.
"""


def lcs(first, second):
    n, m = len(first), len(second)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    sequence = []
    i, j = n, m
    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            sequence.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    sequence.reverse()
    return dp[n][m], ''.join(sequence)


if __name__ == '__main__':
    first = 'AGGTAB'
    second = 'GXTXAYB'
    length, sequence = lcs(first, second)
    print('String 1:', first)
    print('String 2:', second)
    print('LCS:', sequence)
    print('Length:', length)
