#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
        
    mergeLists = SinglyLinkedList()
    if head1.data < head2.data:
        mergeLists.head = head1
        head1 = head1.next
    else:
        mergeLists.head = head2
        head2 = head2.next
        
    temp_node = mergeLists.head
        
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            temp_node.next = head1
            head1 = head1.next
        else:
            temp_node.next = head2
            head2 = head2.next
        temp_node = temp_node.next
        
    if head1 is not None:
        temp_node.next = head1
    else:
        temp_node.next = head2
    
   
    return mergeLists.head