#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts the following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

#---------------------------------------------------------------------------------------------
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    visited = set()
    queue = deque([(startX, startY, 0)])

    while queue:
        x, y, moves = queue.popleft()
        if x == goalX and y == goalY:
            return moves

        # Explore in all four directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X':
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
                nx += dx
                ny += dy

    return -1  # Goal is unreachable
  #---------------------------------------------------------------------------------------------
                
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
