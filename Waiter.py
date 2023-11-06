Waiter

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


def waiter(number, q):
    answers = []
    primes_list = generate_primes(q)
    A = list(number)
    
    for i in range(q):
        B = []
        next_A = []
        current_prime = primes_list[i]
        
        while A:
            current_number = A.pop()
            if current_number % current_prime == 0:
                B.append(current_number)
            else:
                next_A.append(current_number)
            
        answers.extend(reversed(B))
        A = next_A
        
    answers.extend(reversed(A))
    
    return answers
    
    