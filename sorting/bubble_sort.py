"""
Pass (Outer Loop):
- 1st pass: Places the largest element at the last position.
- 2nd pass: Places the 2nd largest element at the 2nd last position.
- And so on... until the array is sorted.
- After i passes, last i elements are in their correct positions.
- If I have n elements, then i = n-1
Comparison (Inner Loop):
- In each pass, compare arr[j] and arr[j+1] for all unsorted elements.
- If arr[j] > arr[j+1], swap them.

If I have K passes I can find the K largest element. Let's say I want to find the 3 largest element, so I can perform 3 passes
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # pythonic swap
                swapped = True
        if not swapped:
            break


arr = [10, 2, 11, 83, 0, 5, 15]
bubble_sort(arr)
print(arr)
