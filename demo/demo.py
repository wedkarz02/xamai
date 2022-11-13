
# Demo file created for functionality testing.
# 
# Adding a parent path of the main package to sys.path
# See README.md for more information.

import sys
import pathlib

package_path = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.insert(0, package_path)


# Actual demo starts here:
import xamai

print(xamai.consts.pi)
print(xamai.exponent(2, 6))

lst = [9, 5, 4, 3, 7, 4, 65, 1, 0]
xamai.bubble_sort(lst)
print(lst)

nums = [1, 2, 3, 4, 5]
nums_normalized = [xamai.normalize(x, 0, 5) for x in nums]
print(nums)
print(nums_normalized)

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(xamai.sum_range(vals, 0, 3))
print(xamai.product_range(vals, 0, 4))

print(xamai.sin_ts(xamai.consts.pi / 4, 10))
print(xamai.sin_ts(xamai.consts.pi / 2, 10))
print(xamai.sin_ts(xamai.consts.pi, 10))