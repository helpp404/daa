"""
EXPERIMENT 13: NAIVE AND KMP STRING MATCHING
THEORY: Find a PATTERN inside a larger TEXT.
Naive matching tries the pattern at every position.
KMP (Knuth-Morris-Pratt) builds an LPS array to avoid rechecking text.
LPS = Longest Proper Prefix that is also a Suffix.

NAIVE ALGORITHM (simple English):
1. Place pattern at each possible starting position in text.
2. Compare characters one by one until mismatch or full match.
3. If all characters match, save that position.
NAIVE TIME: Best O(n) (first-character mismatch each time).
            Worst O(n*m) (long partial matches at many positions).
            Extra space O(1), excluding returned match positions.

KMP ALGORITHM (simple English):
1. Build LPS table for pattern: how much matching prefix can be reused.
2. Scan text and pattern together.
3. On mismatch, move pattern index using LPS instead of restarting.
4. Record matches and use LPS to also detect overlapping matches.
KMP TIME: Best O(n+m), Worst O(n+m).
          Reason: O(m) LPS build + O(n) scan without restarting text.
          Extra space O(m) for LPS, excluding returned positions.
n = length of text; m = length of pattern.

VIVA:
Q1. What is LPS? A. Longest Proper Prefix also equal to a Suffix.
Q2. KMP advantage? A. Does not compare old text characters repeatedly.
Q3. Can matches overlap? A. Yes. 'ana' is at 1 and 3 in 'banana'.
"""


def naive_search(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    positions = []
    n, m = len(text), len(pattern)
    for start in range(n - m + 1):
        j = 0
        while j < m and text[start + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(start)
    return positions


def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]  # Try shorter previous prefix.
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    lps = build_lps(pattern)
    positions = []
    i = j = 0  # i = text index, j = pattern index.
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]  # Find next match; overlaps allowed.
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions


if __name__ == '__main__':
    text = 'ABABDABACDABABCABAB'
    pattern = 'ABABCABAB'
    print('Text:', text)
    print('Pattern:', pattern)
    print('Naive match positions:', naive_search(text, pattern))
    print('KMP match positions:', kmp_search(text, pattern))
