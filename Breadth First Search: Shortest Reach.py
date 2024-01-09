#!/bin/python3

import math
import os
import random
import re
import sys
#---------------------------------------------------------------------------------------------
from collections import deque

# Complete the 'bfs' function below.
def bfs(n, m, edges, s):
    # Create a dictionary to represent the graph
    graph = {i: [] for i in range(1, n+1)}
    
    # Add edges to the graph
    for u, v in edges: 
        graph[u].append(v)
        graph[v].append(u)
        
    # Initialize distances with -1 for each node
    dist = [-1] * (n + 1)
    # The distance to the start node is 0
    dist[s] = 0
    
    # Initialize queue for BFS
    queue = deque([s])
    
    # Perform BFS
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 6
                queue.append(neighbor)
    
    # Prepare the result, excluding the start node and unreachable nodes marked as -1
    return [dist[i] for i in range(1, n+1) if i != s]

#---------------------------------------------------------------------------------------------

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        # Write the result to the output file, joining the elements with a space
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
