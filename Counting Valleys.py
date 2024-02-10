#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

#---------------------------------------------------------------------------------------------

def countingValleys(steps, path):
    sea_lvl = 0
    val_ct = 0
    
    for step in path:
        if step == 'U': 
            sea_lvl += 1
            if sea_lvl == 0:
                val_ct += 1
        else:
            sea_lvl -= 1
            
    return val_ct

#---------------------------------------------------------------------------------------------
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
