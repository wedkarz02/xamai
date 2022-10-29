
# Main module importing all of the necessary files
# Import this module to your project to start using xamai

try:
    from src.constants import *
    from src.functions import *
except:
    raise ImportError("Module files not found. Make sure all files are included properly.")
