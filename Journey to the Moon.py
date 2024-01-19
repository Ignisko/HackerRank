#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

#---------------------------------------------------------------------------------------------

def journeyToMoon(n, astronaut):
    def iterative_dfs(node, graph, visited):
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                size += 1
                for neighbor in graph[current]:
                    stack.append(neighbor)
        return size

    graph = {i: [] for i in range(n)}
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    country_sizes = []
    for i in range(n):
        if not visited[i]:
            country_sizes.append(iterative_dfs(i, graph, visited))

    total_pairs = 0
    for i in range(len(country_sizes)):
        total_pairs += country_sizes[i] * (n - country_sizes[i])
        n -= country_sizes[i]

    return total_pairs
#---------------------------------------------------------------------------------------------


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
