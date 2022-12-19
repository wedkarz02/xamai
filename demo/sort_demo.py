
# Demo file created for sorting algorithms testing.
# 
# Adding a parent path of the main package to sys.path
# See README.md for more information.

import sys
import pathlib

package_path = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.insert(0, package_path)


# Actual demo starts here:
import xamai

unsorted_values = [4, 2, 8, 5, 9, 0, 7, 1, 3, 6]
print(f"unsorted values: {unsorted_values}")

sorted_bubble = xamai.bubble_sort(unsorted_values)
print(f"bubble sort: {unsorted_values}")

unsorted_values = [4, 2, 8, 5, 9, 0, 7, 1, 3, 6]

sorted_bubble = xamai.quick_sort(unsorted_values, 0, len(unsorted_values) - 1)
print(f"bubble sort: {unsorted_values}")
