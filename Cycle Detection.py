#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    faster = head
    
    while faster and faster.next:
        head = head.next
        faster = faster.next.next
        if head == faster:
            return 1
    
    return 0

if __name__ == '__main__':