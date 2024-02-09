#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

#---------------------------------------------------------------------------------------------

def beautifulDays(i, j, k):
    bd_count = 0
    for day in range(i, j + 1):
        # Calculate the reverse of the current day
        reverse_day = int(str(day)[::-1])
        # Calculate the absolute difference
        difference = abs(day - reverse_day)
        # Check if the difference is divisible by k
        if difference % k == 0:
            bd_count += 1
    return bd_count

#---------------------------------------------------------------------------------------------    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
