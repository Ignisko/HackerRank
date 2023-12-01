#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def calculateSwaps(arr, sorted_arr, positions):
    swaps = 0
    for i in range(len(arr)):
        while positions[sorted_arr[i]] != i:
            swaps += 1
            swap_idx = positions[sorted_arr[i]]
            positions[sorted_arr[i]], positions[sorted_arr[swap_idx]] = positions[sorted_arr[swap_idx]], positions[sorted_arr[i]]
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
    return swaps
                
def lilysHomework(arr):
    positions = {value: idx for idx, value in enumerate(arr)}
    sorted_arr_asc = sorted(arr)
    sorted_arr_dsc = sorted(arr, reverse=True)
    
    return min(calculateSwaps(arr[:], sorted_arr_asc, positions.copy()),
               calculateSwaps(arr[:], sorted_arr_dsc, positions.copy()))
               
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
