#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = list(s)
    changed = [False] * n  # Track if the digit has been changed.
    # First pass: Make the number a palindrome.
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if k > 0:
                s[i] = s[n - 1 - i] = max(s[i], s[n - 1 - i])
                changed[i] = changed[n - 1 - i] = True
                k -= 1
            else:
                return '-1'

    # Second pass: Maximize the number.
    i = 0
    while i < n // 2 and k > 0:
        # If it's not already the maximum digit.
        if s[i] != '9':
            # If we've changed this digit before, it only costs 1 change to set it to '9'.
            if changed[i] or changed[n - 1 - i]:
                s[i] = s[n - 1 - i] = '9'
                k -= 1
            # If we haven't changed it before, it costs 2 changes.
            elif k > 1:
                s[i] = s[n - 1 - i] = '9'
                k -= 2
        i += 1

    # If there's an odd number of digits, maximize the middle one if possible.
    if n % 2 == 1 and k > 0:
        s[n // 2] = '9'

    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
