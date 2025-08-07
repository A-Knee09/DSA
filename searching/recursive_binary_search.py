"""
Binary search using recursion, not much changes except for the parameters
"""


def binary_search(arr, target, start, end):
    if start > end:
        print(f"'{target}' not found in the array")
        return

    middle = start + (end - start) // 2

    if arr[middle] == target:
        print(f"'{target}' found at index '{middle}'")
        return

    elif target < arr[middle]:
        return binary_search(arr, target, start, middle - 1)

    else:
        return binary_search(arr, target, middle + 1, end)


# Usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 12
binary_search(arr, target, 0, len(arr) - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1
start = 0
end = len(arr) - 1

binary_search(arr, target, start, end)
