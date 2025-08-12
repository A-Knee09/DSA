"""
Insertion Sort Algorithm:
- Treats the first element as a sorted portion.
- For each pass (starting from index 1):
    1. Take the current element (key).
    2. Compare it with elements in the sorted portion (to its left).
    3. Shift elements to the right until the correct position for 'key' is found.
    4. Insert 'key' at that position.
- Best case: O(n) when array is already sorted.
- Worst case: O(n^2) when array is in reverse order.
"""


def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # Shifting elements greater than the key
        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [10, 2, 11, 83, 0, 5, 15]
insertion_sort(arr)
print(arr)
