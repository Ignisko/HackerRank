#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#---------------------------------------------------------------------------------------------
from functools import reduce
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def getTotalX(a, b):
    # Calculate the lcm for the array a
    lcm_a = reduce(lcm, a)

    # Calculate the gcd for the array b
    gcd_b = reduce(gcd, b)

    # Counter for the number of integers that are factors of all elements of b and
    # that are multiples of all elements of a
    integer_ct = 0

    # Check multiples of the lcm up to the gcd
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            integer_ct += 1
        multiple += lcm_a

    return integer_ct
  
  #---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
