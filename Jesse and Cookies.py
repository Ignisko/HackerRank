#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq

def cookies(k, A):
    if len(A) < 2:
        return 0 if A and A[0] >= k else -1

    heapq.heapify(A)  # Convert list to a min-heap in-place
    count = 0

    while A[0] < k:
        if len(A) < 2:
            return -1

        new_cookie = heapq.heappop(A) + 2 * heapq.heappop(A)
        heapq.heappush(A, new_cookie)
        count += 1

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
