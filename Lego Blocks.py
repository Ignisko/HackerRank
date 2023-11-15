Lego Blocks

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

MODULO = 10 ** 9 + 7

def legoBlocks(n, m):
    row = [0] * (m + 1)

    for i in range(1, min(m, 4) + 1):
        row[i] = 2**(i - 1)

    if m >= 5:
        for i in range(5, m + 1):
            row[i] = (row[i - 1] + row[i - 2] + row[i - 3] + row[i - 4]) % MODULO

    total = row.copy()

    for _ in range(2, n + 1):
        for i in range(1, m + 1):
            total[i] = (row[i] * total[i]) % MODULO

    solid = [0] * (m + 1)
    solid[1] = 1

    for ww in range(2, m + 1):
        unsolid_sum = sum((solid[i] * total[ww - i]) % MODULO for i in range(1, ww))
        solid[ww] = (total[ww] - unsolid_sum) % MODULO

    return solid[m] % MODULO
