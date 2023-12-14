#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#


#---------------------------------------------------------------------------------------------

from operator import mul
from functools import reduce

def beadOrnaments(b):
    MOD = 10**9 + 7

    # Calculate the product of each bead count raised to the power of itself minus one
    product_of_powers = reduce(mul, (count ** (count - 1) for count in b), 1)

    # Cayley's formula: Total beads raised to the power of the number of colors minus two
    cayleys_formula = sum(b) ** (len(b) - 2)

    # The number of distinct ornaments, taking into account the modulo
    num_of_ornaments = int(product_of_powers * cayleys_formula) % MOD
    
    return num_of_ornaments


#---------------------------------------------------------------------------------------------

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        b_count = int(input().strip())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()

