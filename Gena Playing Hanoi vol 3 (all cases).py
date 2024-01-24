#!/bin/python3

import os
import math

#---------------------------------------------------------------------------------------------
from copy import deepcopy

'''
FUNCTION bfs(rods, n):
    Initialize start state and visited set
    Initialize a queue and add the start state
    WHILE queue is not empty:
        Get current state and depth
        IF goal state is reached:
            RETURN depth
        FOR each possible move from current state:
            IF the new state is not visited:
                Mark as visited and add to queue
    RETURN -1 if goal state is not reached

READ n
INITIALIZE rods
FOR each disk, UPDATE rods
CALL bfs(rods, n) and PRINT result
'''

def solve_hanoi(N, a):
    end = [[] for _ in range(4)]  # End state
    initial = [[] for _ in range(4)]  # Initial state

    # Initialize the end and initial states
    for i in range(N - 1, -1, -1):
        end[a[i] - 1].append(i + 1)
        initial[0].append(i + 1)

    states = {0: initial}  # States to be checked
    visited = {','.join(map(str, initial)): 1}  # States already visited
    nextlevel = {}  # Next level states

    i = 0
    z = 0
    ind = 1
    check = 0

    # Maximum steps: 2^N
    while i <= math.pow(2, N):
        for k in range(4):
            for j in range(4):
                temp = deepcopy(states[z])
                if temp[k] and j != k:
                    move_disk = temp[k].pop()
                    if not temp[j] or (temp[j] and temp[j][-1] > move_disk):
                        temp[j].append(move_disk)
                        key = ','.join(map(str, temp))
                        if key not in visited:
                            states[ind] = temp
                            visited[key] = 1
                            nextlevel[ind] = 1
                            ind += 1
                            if temp == end:
                                return i + 1
                                check = 1
                                break
            if check == 1:
                break
        if check == 1:
            break
        del states[z]
        z += 1
        if z in nextlevel:
            nextlevel = {}
            i += 1

    return -1  # Return -1 or an appropriate value if no solution is found

#---------------------------------------------------------------------------------------------


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = solve_hanoi(n, loc)

    fptr.write(str(res) + '\n')

    fptr.close()
