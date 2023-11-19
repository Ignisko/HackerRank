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

    transmitters = 0
    i = 0  # Index to traverse the houses

    while i < len(x):
        transmitters += 1
        location = x[i]  # Place the transmitter at this house
        while i < len(x) and x[i] <= location + k:
            i += 1
        i -= 1  # Move back to the house within transmitter range

        location = x[i]  # Place the next transmitter
        while i < len(x) and x[i] <= location + k:
            i += 1

    return transmitters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
