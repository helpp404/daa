"""
EXPERIMENT 1: BUBBLE SORT
THEORY: Compare neighboring numbers. If they are in the wrong order, swap.
After each pass, the biggest remaining number 'bubbles' to the end.

ALGORITHM (simple English):
1. Start from the first element.
2. Compare every neighboring pair; swap if left > right.
3. After one pass, the largest remaining item is in place.
4. Repeat, but stop early if no swaps happened in a pass.

TIME COMPLEXITY:
Best: O(n) -- Already sorted, so one comparison pass and zero swaps.
Worst: O(n^2) -- Reverse sorted; many passes with many comparisons.
Space: O(1) -- Swaps happen inside the original list.

VIVA:
Q1. Why Bubble Sort? A. Large items 'bubble up' to the right.
Q2. Is it stable? A. Yes, because equal values are not swapped.
Q3. Why best case O(n)? A. 'swapped' flag detects a sorted list early.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted.
    return arr


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", numbers)
    print("Sorted:", bubble_sort(numbers))
