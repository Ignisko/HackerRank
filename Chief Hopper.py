Chief Hopper
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    energy = 0
    for height in reversed(arr):
        energy = (energy + 1 + height) // 2
    return energy
        
        