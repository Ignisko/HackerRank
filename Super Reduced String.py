Super Reduced String

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    new_string = []
    for character in s:
        if new_string and new_string[-1] == character:
            new_string.pop()
        else:
            new_string.append(character)
    if not new_string:
        return "Empty String"
        
    else:
        return ''.join(new_string)
