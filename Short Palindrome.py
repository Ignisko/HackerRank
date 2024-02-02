#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as a parameter.

#---------------------------------------------------------------------------------------------

 def shortPalindrome(s):
    MOD = 10**9 + 7
    letter_ct = [0] * 26       # Counts of individual letters
    pair_ct = [[0] * 26 for _ in range(26)]  # Counts of pairs of letters
    single_ct = [0] * 26       # Count of single letters for the third character in the tuple
    tot_ct = 0                 # Total count of palindromic tuples

    for char in s:
        index = ord(char) - ord('a')

        # Update the total count for palindromic tuples ending with the current character.
        tot_ct = (tot_ct + single_ct[index]) % MOD

        # Update single_ct for each character using pair_ct.
        # This is for the scenario where the current character is the third in the tuple.
        for j in range(26):
            single_ct[j] = (single_ct[j] + pair_ct[j][index]) % MOD

        # Update pair_ct for each character using letter_ct.
        # This is for the scenario where the current character is the second in the tuple.
        for j in range(26):
            pair_ct[j][index] = (pair_ct[j][index] + letter_ct[j]) % MOD

        # Update letter_ct for the current character.
        # This is for the scenario where the current character is the first in the tuple.
        letter_ct[index] = (letter_ct[index] + 1) % MOD

    return tot_ct

#---------------------------------------------------------------------------------------------
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
