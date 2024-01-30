#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

#---------------------------------------------------------------------------------------------
import heapq

def getCost(g_nodes, g_from, g_to, g_weight):
    graph = {i: [] for i in range(1, g_nodes + 1)}
    for i in range(len(g_from)):
        graph[g_from[i]].append((g_to[i], g_weight[i]))
        graph[g_to[i]].append((g_from[i], g_weight[i]))
        
    fare = [float('inf')] * (g_nodes + 1)
    fare[1] = 0
    
        
    pq = [(0, 1)]
    
    while pq:
        current_fare, station = heapq.heappop(pq)
            
        for neighbor, weight in graph[station]:
            
            new_fare = max(current_fare, weight)
            if new_fare < fare[neighbor]:
                fare[neighbor] = new_fare
                heapq.heappush(pq, (new_fare, neighbor))
                
    if fare[g_nodes] == float('inf'):
        print("NO PATH EXISTS")
    else:
        print(fare[g_nodes])
  
#---------------------------------------------------------------------------------------------
            
        
if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
