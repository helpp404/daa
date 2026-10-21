"""
EXPERIMENT 2: INSERTION SORT
THEORY: Like sorting cards in your hand. Take the next number and
insert it at the correct place among the already sorted numbers.

ALGORITHM (simple English):
1. Consider the first element sorted.
2. Store the next element in 'key'.
3. Shift every bigger element in the sorted portion one place right.
4. Insert key into its right position. Repeat for all elements.

TIME COMPLEXITY:
Best: O(n) -- Already sorted; each key needs just one comparison.
Worst: O(n^2) -- Reverse sorted; each key shifts past all earlier items.
Space: O(1) -- Only a few temporary variables.

VIVA:
Q1. Is Insertion Sort stable? A. Yes, equal items keep their order.
Q2. Where is it useful? A. For small or almost sorted lists.
Q3. In-place sorting? A. Yes; no separate sorting array is needed.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Value we are placing in its right position.
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift bigger item right.
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]
    print("Original:", numbers)
    print("Sorted:", insertion_sort(numbers))
