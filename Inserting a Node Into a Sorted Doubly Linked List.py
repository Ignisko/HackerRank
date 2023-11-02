#Inserting a Node Into a Sorted Doubly Linked List

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    
    # If the list is empty or insert at the beginning
    if not llist or data < llist.data:
        new_node.next = llist
        if llist:
            llist.prev = new_node
        return new_node
    
    # Find the position to insert
    current = llist
    while current.next and current.next.data < data:
        current = current.next
        
    # Linking the new node in its place
    new_node.next = current.next
    if new_node.next:
        new_node.next.prev = new_node
    current.next = new_node
    new_node.prev = current
    
    return llist
