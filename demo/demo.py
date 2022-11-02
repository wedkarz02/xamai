
import sys
sys.path.append("..")

import xamai

print(xamai.pi)
print(xamai.exponent(2, 6))

lst = [9, 5, 4, 3, 7, 4, 65, 1, 0]
xamai.bubble_sort(lst)
print(lst)
