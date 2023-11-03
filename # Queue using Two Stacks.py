# Queue using Two Stacks
# Define the Stack class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


# Instantiate the stacks
stack1 = Stack()
stack2 = Stack()

# Define the transfer_elements function
def transfer_elements():
    if stack2.isEmpty():
        while not stack1.isEmpty():
            stack2.push(stack1.pop())

# Read the number of queries
q = int(input().strip())

# Process each query
for _ in range(q):
    query = list(map(int, input().strip().split()))
    query_type = query[0]
    if query_type == 1:
        element = query[1]
        stack1.push(element)
    elif query_type == 2:
        transfer_elements()
        stack2.pop()  # Corrected this line
    elif query_type == 3:
        transfer_elements()  # Corrected this line
        print(stack2.peek())
