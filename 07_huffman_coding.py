"""
EXPERIMENT 7: HUFFMAN CODING (LOSSLESS TEXT COMPRESSION)
THEORY: Give SHORT codes to frequent characters and LONG codes to rare
characters. The resulting codes are prefix-free, so decoding is unique.

ALGORITHM (simple English):
1. Count the frequency of each character in text.
2. Put all characters into a min-heap (priority queue).
3. Remove two least frequent nodes, combine under a new parent.
4. Put the parent back; repeat until there is just one root node.
5. Walk the tree: left=0, right=1 to assign binary codes.
6. Encode the text using these codes.

TIME COMPLEXITY (n = input characters, k = unique characters,
                 L = number of bits in final encoded output):
Best: O(n + k log k + L) -- Count, heap operations, make encoded output.
Worst: O(n + k log k + L) -- Same phases; L may reach O(n*k).
Reason: Encoding time also depends on the total code length L.
Space: O(k + L) -- Huffman tree/codes and encoded output (excluding input).

VIVA:
Q1. Lossy or lossless? A. Lossless: exact original can be recovered.
Q2. Why min-heap? A. Quickly find two smallest frequencies.
Q3. Prefix-free? A. No character code is a prefix of another code.
"""

from collections import Counter
from itertools import count
import heapq


def huffman_codes(text):
    if not text:
        return {}
    frequencies = Counter(text)
    heap = []
    order = count()  # Prevent comparisons of tree nodes on frequency ties.
    for char, freq in frequencies.items():
        heapq.heappush(heap, (freq, next(order), char))

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        parent = (left, right)
        heapq.heappush(heap, (f1 + f2, next(order), parent))

    root = heap[0][2]
    codes = {}

    def make_codes(node, path):
        if isinstance(node, str):
            codes[node] = path or '0'  # Special case: one unique character.
            return
        make_codes(node[0], path + '0')
        make_codes(node[1], path + '1')

    make_codes(root, '')
    return codes


def encode(text, codes):
    return ''.join(codes[c] for c in text)


def decode(bits, codes):
    lookup = {code: char for char, code in codes.items()}
    chars = []
    current = ''
    for bit in bits:
        current += bit
        if current in lookup:
            chars.append(lookup[current])
            current = ''
    if current:
        raise ValueError('Incomplete bit sequence')
    return ''.join(chars)


if __name__ == '__main__':
    text = 'banana bandana'
    codes = huffman_codes(text)
    bits = encode(text, codes)
    print('Original:', text)
    print('Codes:', codes)
    print('Encoded:', bits)
    print('Decoded:', decode(bits, codes))
