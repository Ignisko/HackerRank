#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()  # To store unique weights of uniform substrings
    prev_char = ''    # To keep track of the previous character
    count = 0         # To count consecutive characters
    
    for char in s:
        weight = ord(char) - ord('a') + 1  # Calculate weight of current character
        
        if char == prev_char:
            count += 1
        else:
            count = 1
            prev_char = char
        
        weights.add(weight * count)  # Add the calculated weight to the set
    
    results = ['Yes' if q in weights else 'No' for q in queries]  # Check if the queries match any weight
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
