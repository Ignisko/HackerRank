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

#---------------------------------------------------------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node.count
                
def contacts(queries):
    trie = Trie()
    results = []
    for operation, name in queries:
        if operation == "add":
            trie.insert(name)
        elif operation == "find":
            results.append(trie.find(name))
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
