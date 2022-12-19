
from .functions import swap


def bubble_sort(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                swap(array, j, j + 1)


# TODO (wedkarz): add documentation
def quick_sort(array: list, start: int, end: int):
    if start >= end or start < 0:
        return

    pivot_index = _partition_qsort(array, start, end)

    quick_sort(array, pivot_index + 1, end)
    quick_sort(array, start, pivot_index - 1)


def _partition_qsort(array: list, start: int, end: int):
    pivot_index = start
    pivot_value = array[end]

    for i in range(start, end):
        if array[i] < pivot_value:
            swap(array, i, pivot_index)
            pivot_index += 1
    
    swap(array, pivot_index, end)
    return pivot_index

