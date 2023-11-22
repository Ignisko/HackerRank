#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k

#
def hackerlandRadioTransmitters(x, k):
    x.sort()  # Sort the house locations
    n = len(x)
    num_transmitters = 0
    i = 0

    while i < n:
        num_transmitters += 1
        loc = x[i] + k
        while i < n and x[i] <= loc:  # Find the farthest house to place the transmitter
            i += 1
        loc = x[i-1] + k
        while i < n and x[i] <= loc:  # Move to the first house out of current transmitter's range
            i += 1

    return num_transmitters


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
