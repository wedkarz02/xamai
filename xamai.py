
# Main module importing all of the necessary files
# Import this module to your project to start using xamai

import sys

try:
    from src.constants import *
    from src.functions import *
    from src.sorting import *
except ModuleNotFoundError:
    sys.exit("[ERROR]: Module files not found. Make sure all files are included properly.")
