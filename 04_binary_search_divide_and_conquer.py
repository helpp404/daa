"""
EXPERIMENT 4: Binary Search using Divide and Conquer

THEORY (simple English):
Binary Search finds an element in a SORTED list. It checks the middle
value and ignores the half where the target cannot be present.
This is called Divide and Conquer because the search range is halved.

ALGORITHM (say these steps in viva):
1. Keep two pointers: low at first index and high at last index.
2. Find middle index = (low + high) // 2.
3. If middle element equals target, return its index.
4. If target is smaller, search only the left half.
5. Otherwise, search only the right half.
6. Repeat until found or low > high (not found).

TIME COMPLEXITY:
Best case: O(1) - target is at the middle in the first check.
Worst case: O(log n) - every comparison halves the remaining search range.
SPACE COMPLEXITY: O(1) - iterative version uses only low, high, and mid.

IMPORTANT VIVA QUESTIONS:
Q1. Why must the array be sorted?
A. We decide which half to discard by comparing the target with the middle.
   This only works correctly when the data is sorted.
Q2. Why is Binary Search faster than Linear Search?
A. Binary Search removes half of the remaining elements each step: O(log n).
   Linear Search may check every element: O(n).
Q3. What is the difference between iterative and recursive Binary Search?
A. Both take O(log n) worst-case time. Iterative uses O(1) extra space,
   while recursive uses O(log n) stack space in the worst case.
"""


def binary_search(arr, target):
    low = 0                     # First position
    high = len(arr) - 1         # Last position

    while low <= high:          # Continue while search area exists
        mid = (low + high) // 2 # Middle index (// means integer division)

        if arr[mid] == target:
            return mid         # Target found; return position (0-based)
        elif target < arr[mid]:
            high = mid - 1     # Discard right half, including middle
        else:
            low = mid + 1      # Discard left half, including middle

    return -1                   # Target not found


if __name__ == "__main__":
    # INPUT: Change these values to test another sorted list and target.
    numbers = [2, 5, 8, 12, 16, 23, 38, 56]
    target = 23

    index = binary_search(numbers, target)
    if index == -1:
        print("Element not found")
    else:
        print("Element found at index:", index)
        print("Position (counting from 1):", index + 1)

    # OPTIONAL KEYBOARD INPUT (remove # from both lines and replace above input):
    # numbers = list(map(int, input("Enter SORTED numbers separated by spaces: ").split()))
    # target = int(input("Enter element to search: "))
