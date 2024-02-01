#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
#---------------------------------------------------------------------------------------------
    # Pair each price with its year, then sort the pairs by price
    indexed_prices = list(enumerate(price))
    indexed_prices.sort(key=lambda x: x[1])

    # Initialize minimum loss to a very large number
    min_loss = float('inf')

    # Iterate through the sorted prices
    for i in range(len(indexed_prices) - 1):
        # Calculate the difference between consecutive prices
        current_loss = indexed_prices[i + 1][1] - indexed_prices[i][1]

        # Check if this is a valid transaction (buy before sell) and if the current loss is less than the minimum loss found so far
        if indexed_prices[i + 1][0] < indexed_prices[i][0] and current_loss < min_loss:
            min_loss = current_loss

    return min_loss

#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
