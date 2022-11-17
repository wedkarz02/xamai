
# Demo file created for testing constant values.
# 
# Adding a parent path of the main package to sys.path
# See README.md for more information.

import sys
import pathlib

package_path = str(pathlib.Path(__file__).resolve().parents[2])
sys.path.insert(0, package_path)


# Actual demo starts here:
import xamai
