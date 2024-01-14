#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):

#---------------------------------------------------------------------------------------------
    
    ctcs_list = []
    results = []
    
    for abracadabra_query in queries:
        operation, name = abracadabra_query
        
        if operation == "add":
            ctcs_list.append(name)
        elif operation == "find":
            count = sum(contact.startswith(name) for contact in ctcs_list)
            results.append(count)
    return results

#---------------------------------------------------------------------------------------------
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
