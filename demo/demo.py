
# Demo file created for functionality testing

import os
import sys
import inspect

# Importing a parent directory
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

# Actial demo:
import xamai

print(xamai.pi)
print(xamai.exponent(2, 6))

lst = [9, 5, 4, 3, 7, 4, 65, 1, 0]
xamai.bubble_sort(lst)
print(lst)
