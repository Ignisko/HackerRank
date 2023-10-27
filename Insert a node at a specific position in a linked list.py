

SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    
    new_node = SinglyLinkedListNode(data)
    current = llist
    count = 0
    
    while count < position - 1 and current:
        current = current.next
        count += 1
    
    if current:
        new_node.next = current.next
        current.next = new_node
    
    return llist