The Maximum Subarray
import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def maxSubarray(arr):
    # Handle the case where the array is empty
    if not arr:
        return [0, 0]
    
    # Initialize the variables for Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    # Initialize the max subsequence sum with the first element or 0 if it's negative
    max_subseq = max(0, arr[0])
    
    # Apply Kadane's algorithm for maximum subarray sum
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    
    # Calculate maximum subsequence sum
    for x in arr[1:]:
        if x > 0:
            max_subseq += x

    # Handle the case where all elements are negative for the subsequence sum
    if max_subseq == 0:
        max_subseq = max(arr)
    
    return [max_so_far, max_subseq]

# Example usage
arr = [-1, 2, 3, -4, 5, 10]
print(maxSubarray(arr))  # Output should be [16, 20]
