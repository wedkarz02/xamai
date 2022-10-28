
# Main module importing all of the necessary files
# Import this module to your project to start using xamai

try:
    from src.constants import *
    from src.functions import *
except:
    raise ImportError("Module files not found. Make sure all files are included properly.")

from random import randrange, random

min = 0
max = 100
lst = [randrange(min, max - 1) + random() for _ in range(15)]

lst_normalized = [normalize(x, min, max) for x in lst]
print(lst)
print(lst_normalized)
