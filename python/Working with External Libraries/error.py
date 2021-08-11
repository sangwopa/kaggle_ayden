from math import *
from numpy import *
print(pi, log(32, 2))

# Traceback (most recent call last):
#   File "c:\Users\admin\Documents\GitHub\kaggle_ayden\Working with External Libraries\error.py", line 3, in <module>
#     print(pi, log(32, 2))
# TypeError: return arrays must be of ArrayType

# modle 'math' and 'numpy' they have a module with the same name "log".
# But they have different semantics, so they throw an error.

from math import log, pi
from numpy import asarray

# A good compromise is to import only the specific things we'll need from each module.