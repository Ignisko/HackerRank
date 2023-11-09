Two Characters

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def is_alternating(str):
    for i in range(len(str) -1):
        if str[i] == str[i+1]:
            return False
    return True
            
        
def alternate(s):
    unique_char = list(set(s))
    longest = 0
    
    for i in range(len(unique_char)):
        for j in range(i+ 1, len(unique_char)):
            filtered_str = ''.join([char for char in s if char == unique_char[i] or char == unique_char[j]])
            if is_alternating(filtered_str):
                longest = max(longest, len(filtered_str))
            
            """
            ALTERNATIVE SOLUTION
            # Start with an empty list to collect the characters
filtered_chars = []

# Loop through each character in the string 's'
for char in s:
    # Check if the character is one of the two we're interested in
    if char == unique_characters[i] or char == unique_characters[j]:
        # If it is, add it to the list
        filtered_chars.append(char)

# Join the collected characters into a string without any separators
filtered_str = ''.join(filtered_chars)
            """
    
    return longest
    
    