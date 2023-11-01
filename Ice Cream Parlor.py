#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    seen = {}
    for i, price in enumerate(arr):
        complement = m - price
        if complement in seen:
            return sorted([seen[complement] + 1, i+1])
        seen[price] = i
