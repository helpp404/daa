"""
EXPERIMENT 14: RABIN-KARP STRING MATCHING USING HASHING
THEORY: Compare numerical HASH of pattern with the hash of each same-
length window in text. Rolling hash updates quickly for next window.
If hashes match, compare actual characters to confirm a real match.

ALGORITHM (simple English):
1. Calculate hash of pattern and first equal-length text window.
2. If hashes match, compare the actual strings (collision check).
3. Slide the window right by one character; update rolling hash.
4. Repeat until all windows are checked.

TIME COMPLEXITY (n = text length, m = pattern length):
Best: O(n+m) -- Hashes mostly differ; every rolling update is O(1).
Worst: O(n*m) -- Many collisions/full matches require O(m) checks.
Space: O(1) extra, excluding the returned list of matching positions.

VIVA:
Q1. What is collision? A. Different strings giving equal hashes.
Q2. Why compare strings after hash match? A. To avoid false matches.
Q3. Rolling hash advantage? A. Next window hash updates in O(1).
"""


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []

    base = 256
    prime = 101  # Modulus to keep hash values small.
    high_power = pow(base, m - 1, prime)
    pattern_hash = window_hash = 0

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    matches = []
    for start in range(n - m + 1):
        if pattern_hash == window_hash:
            # Hash collision is possible, so check actual characters.
            if text.startswith(pattern, start):
                matches.append(start)
        if start < n - m:
            # Remove left character, shift, add next right character.
            window_hash = ((window_hash - ord(text[start]) * high_power)
                           * base + ord(text[start + m])) % prime
    return matches


if __name__ == '__main__':
    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    print('Text:', text)
    print('Pattern:', pattern)
    print('Match positions:', rabin_karp(text, pattern))
