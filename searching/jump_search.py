"""
Jump Search is an algorithm for finding an element in a sorted array. Instead of searching one element at a time (like Linear Search), it jumps ahead by fixed steps (block size) to find the range where the target may exist, then performs a linear search within that block.

Steps:
1. Determine the optimal jump (block size) as √n, where n is array length.
2. Jump forward until the target is <= current block's last element or until the end of the array is reached.
3. Perform a linear search within the identified block.

Advantages:
- Faster than linear search for large sorted datasets.
- Easy to implement.

Limitations:
- Works only on sorted arrays.
- Not as efficient as Binary Search in most cases.

Time Complexity:
- Best case: O(1)
- Average/Worst case: O(√n)
Space Complexity: O(1)
"""

import math


def jump_search(arr, target):

    n = len(arr)
    jump = int(math.sqrt(n))  # Optimal jump size
    prev = 0

    # Jump ahead while the target is greater than the last element of the block

    while prev < target and arr[min(jump, n) - 1] < target:

        prev = jump
        jump += int(math.sqrt(n))

        if prev >= n:
            return -1  # Target not found

    # Linear Search within the identified block
    while prev < min(jump, n) and arr[prev] < target:
        prev += 1
        if prev >= n:
            return -1

    # Check if the target is found
    if prev < n and arr[prev] == target:
        return prev

    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15
index = jump_search(arr, target)

if index != -1:
    print(f"Target '{target}' found at index {index}")
else:
    print(f"Target '{target}' not found")
