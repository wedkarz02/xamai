
from .functions import swap


def bubble_sort(array: list):
    # Sorts the array values using
    # the Bubble sorting algorithm
    # https://en.wikipedia.org/wiki/Bubble_sort

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                swap(array, j, j + 1)


def quick_sort(array: list, start: int, end: int):
    # Sorts the array values using
    # the Lomuto Partition scheme
    # of the Quick sorting algorithm
    # https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

    if start >= end or start < 0:
        return

    pivot_index = _lomuto_partition(array, start, end)

    quick_sort(array, pivot_index + 1, end)
    quick_sort(array, start, pivot_index - 1)


def _lomuto_partition(array: list, start: int, end: int):
    # Partition function used in the
    # Lomuto scheme.
    # Should not be used outside of the quick_sort function

    pivot_index = start
    pivot_value = array[end]

    for i in range(start, end):
        if array[i] < pivot_value:
            swap(array, i, pivot_index)
            pivot_index += 1
    
    swap(array, pivot_index, end)
    return pivot_index

