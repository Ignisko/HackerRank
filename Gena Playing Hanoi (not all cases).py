#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

#---------------------------------------------------------------------------------------------

def hanoi(posts):
    moves = 0
    n = len(posts)
    rod_positions = [1] * n  # Initial expected positions of all disks

    for disk in range(n, 0, -1):
        if posts[disk - 1] != rod_positions[disk - 1]:
            # Calculate moves for this disk and all smaller disks
            moves += 2 ** (disk - 1)
            # Update expected positions for smaller disks
            for j in range(disk - 1):
                rod_positions[j] = posts[disk - 1]
    
    return moves
  
#---------------------------------------------------------------------------------------------

    
if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()
