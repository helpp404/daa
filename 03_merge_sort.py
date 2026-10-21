"""
EXPERIMENT 3: MERGE SORT
THEORY: Divide and Conquer. Split a list into halves, recursively sort
both halves, and merge those sorted halves into one sorted list.

ALGORITHM (simple English):
1. If list has 0 or 1 items, return it (already sorted).
2. Divide list into left and right halves.
3. Recursively sort both halves.
4. Merge the two sorted lists by choosing smaller front elements.

TIME COMPLEXITY:
Best: O(n log n) -- Even sorted data is split and merged at every level.
Worst: O(n log n) -- log n levels; total O(n) merging per level.
Space: O(n) -- Temporary lists during merging.

VIVA:
Q1. Which technique? A. Divide and Conquer.
Q2. Is it stable? A. Yes, with <= when comparing equal elements.
Q3. Why extra space? A. Because temporary lists are created to merge.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])   # Add the remaining elements.
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", numbers)
    print("Sorted:", merge_sort(numbers))
