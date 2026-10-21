"""
EXPERIMENT 4: IMPLEMENTATION & ANALYSIS USING DIVIDE AND CONQUER
NOTE: Index does not name a particular problem. This file demonstrates
Divide and Conquer by finding MINIMUM and MAXIMUM together. Confirm your
teacher's expected problem if they have specified another example.

THEORY: Divide a problem into small parts, solve them, combine answers.

ALGORITHM (simple English):
1. If there is only one number, it is both minimum and maximum.
2. Otherwise divide the given part into left and right halves.
3. Find min and max of each half recursively.
4. Combine: take the smaller minimum and the bigger maximum.

TIME COMPLEXITY:
Best: O(n) -- Every element must be examined even if already sorted.
Worst: O(n) -- T(n) = 2T(n/2) + O(1) = O(n).
Space: O(log n) -- Recursion stack because halves are balanced.

VIVA:
Q1. Three steps? A. Divide, Conquer, Combine.
Q2. Examples? A. Merge Sort, Quick Sort, Binary Search.
Q3. Base case? A. One element is both its own min and max.
"""


def find_min_max(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    numbers = [7, 2, 9, 4, 1, 8]
    low, high = find_min_max(numbers, 0, len(numbers) - 1)
    print("List:", numbers)
    print("Minimum:", low)
    print("Maximum:", high)
