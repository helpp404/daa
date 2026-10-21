"""
EXPERIMENT 5: QUICK SORT
THEORY: Divide and Conquer. Choose a pivot. Put smaller/equal elements
on its left, bigger elements on its right, then sort both parts.
Here the LAST element is used as pivot.

ALGORITHM (simple English):
1. Choose last element as pivot.
2. Partition: move items <= pivot left and others right.
3. Pivot reaches its final sorted position.
4. Recursively sort the left and right parts.

TIME COMPLEXITY:
Best: O(n log n) -- Pivot splits array into near-equal halves.
Worst: O(n^2) -- Last pivot always smallest/largest (e.g., sorted list),
                 so splits have 0 and n-1 elements, many levels.
Space: O(log n) best, O(n) worst -- Recursion stack; swaps are in-place.

VIVA:
Q1. What is pivot? A. Element used to partition the array.
Q2. Why worst O(n^2)? A. Extremely unequal partitions every time.
Q3. Is standard Quick Sort stable? A. No, equal elements can move.
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # End of region containing elements <= pivot.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]
    print("Original:", numbers)
    print("Sorted:", quick_sort(numbers, 0, len(numbers) - 1))
