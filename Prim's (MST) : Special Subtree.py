#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#
#---------------------------------------------------------------------------------------------
import heapq

def prims(n, edges, start):
    # Convert edge list to adjacency list
    adj_list = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # Initialize all keys as infinite
    key = {i: float('inf') for i in range(1, n + 1)}
    key[start] = 0

    # Keep track of vertices included in MST
    mstSet = set()

    # Use a heap for vertices not yet included in MST
    heap = [(0, start)]

    while heap:
        # Extract min weight vertex; Add it to the set mstSet
        weight, u = heapq.heappop(heap)
        if u in mstSet:
            continue
        mstSet.add(u)

        # For all adjacent vertices v, update key values and push to the heap
        for v, w in adj_list[u]:
            if v not in mstSet and key[v] > w:
                key[v] = w
                heapq.heappush(heap, (w, v))

    # Sum of weights in MST
    return sum(key.values())
  
#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
