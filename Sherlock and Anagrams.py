Sherlock and Anagrams

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    substring_dict = {}
    
    for length in range(1, len(s) + 1):
        for start in range(len(s)- length + 1):
            substring = s[start:start + length]
            sorted_substring = ''.join(sorted(substring))
            substring_dict[sorted_substring] = substring_dict.get(sorted_substring, 0) + 1
    
    count = 0
    for freq in substring_dict.values():
        count += freq * (freq - 1) // 2
    
    return count