#!/bin/python3

import os
import math

#---------------------------------------------------------------------------------------------
from collections import deque

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


def tuplify(x):
    return tuple(tuple(i) for i in x)

def moves(rods):
    for x in range(4):
        if rods[x]:
            for y in range(4):
                if not rods[y] or rods[y][-1] > rods[x][-1]:
                    yield (x, y)

def do_move(rods, x, y):
    rods = [list(r) for r in rods]
    rods[y].append(rods[x].pop())
    rods[1:4] = sorted(rods[1:4], key=lambda t: t[-1] if t else 0)
    return tuplify(rods)

def bfs(rods, n):
    start = (tuplify(rods), 0)
    visited = set()
    visited.add(start)
    q = deque([start])
    while q:
        cur, depth = q.popleft()
        if all(len(r) == 0 for r in cur[1:]):
            return depth
        for x, y in moves(cur):
            child = do_move(cur, x, y)
            if child not in visited:
                visited.add(child)
                q.append((child, depth + 1))
    return -1

n = int(input())
rods = [[] for _ in range(4)]
for i, disk in enumerate(map(int, input().split())):
    rods[disk-1] = [i] + rods[disk-1]
print(bfs(rods, n))
