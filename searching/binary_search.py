"""
Binary Search Operates on sorted arrays. Time complexity : O(logn)
"""


def binary_search(arr, target):

    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = start + (end - start) // 2

        if arr[middle] == target:
            print(f"Target '{target}' found at index {middle}")
            return

        elif target > arr[middle]:
            start = middle + 1

        else:
            end = middle - 1

    print(f"Target '{target}' not found in the array")
    return


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 12

binary_search(arr, target)
