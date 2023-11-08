The Coin Change Problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Filter out coins larger than the amount n
    c = [coin for coin in c if coin <= n]

    for coin in c:
        for amount in range(coin, n + 1):
            ways[amount] += ways[amount - coin]

    return ways[n]
