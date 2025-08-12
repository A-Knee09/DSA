"""
Sorts a list in ascending order using the Selection Sort algorithm.

Technique:
    - The array is divided into two parts: the sorted part at the left and the unsorted part at the right.
    - Repeatedly find the smallest element in the unsorted part and swap it with the leftmost unsorted element.
    - After each iteration, the sorted part grows by one, and the unsorted part shrinks.
"""


def selection_sort(arr):

    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
