# XAMAI Academic Math and Algorithm Implementation

Detailed description not available yet.<br /><br />

The source for this project is avaliable [here](https://github.com/wedkarz02/xamai).

# Download

To download XAMAI repository run this command:
```bash
git clone https://github.com/wedkarz02/xamai.git
```
or use the "Download ZIP" option from the [GitHub page](https://github.com/wedkarz02/xamai).

# Usage

To use XAMAI properly you need to insert an absolute path of the parent directory of XAMAI to **sys.path** of your script. The way of doing this highly depends on your project setup and XAMAI package location. \
Consider this example:
```
projects/
|
|---- test_project/
|     |
|     |---- main.py
|
|---- xamai/
```
In this example the parent directory of *xamai/* is **projects/**, so in order to use XAMAI in *main.py* you would need to insert an absolute path to **projects/** in **sys.path** of the *main.py* file. \
Since *test_project/* and *xamai/* share the same parent directory the easiest way of doing it would be writing this code snippet in *main.py/* :
```python
import sys
import pathlib

package_path = str(pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, package_path)

# At this point XAMAI is available
# and can be imported as a normal package.
import xamai
```
For more information about the python package system I highly recommend reading [this article](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html) by [Chris Yeh](https://chrisyeh96.github.io/) as well as the [python documentation](https://docs.python.org/3/tutorial/modules.html).
