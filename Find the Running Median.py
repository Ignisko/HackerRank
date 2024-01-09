#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
#---------------------------------------------------------------------------------------------
import heapq

def runningMedian(a):
    max_heap = []  # Min-heap for the smaller half
    min_heap = []  # Min-heap for the larger half
    medians = []   # List to store computed medians
    
    for x in a:
        if not max_heap or x <= -max_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)
        
        # Ensure balance between the two heaps
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        # Calculate the current median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]
        
        medians.append(median)
    
    return medians

#---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    for median in result:
        print(f'{median:.1f}')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
