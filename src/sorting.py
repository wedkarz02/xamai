
from functions import swap

def bubble_sort(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                swap(array, j, j + 1)

