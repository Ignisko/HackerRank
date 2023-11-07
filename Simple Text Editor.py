Simple Text Editor
import sys

def perform_op(operations):
    S = ""
    stack = []
    
    for operation in operations:
        op = operation.split()
        if op[0] == "1":
            stack.append(S)
            S += op[1]
        elif op[0] == "2":
            stack.append(S)
            k = int(op[1])
            S = S[:-k]
        elif op[0] == "3":
            k = int(op[1])
            if k <= len(S):
                print(S[k-1])
            else:
                print("Error: Index out of bounds")
        elif op[0] == "4":
            if stack:
                S = stack.pop()
            else:
                print("Error: No operation to undo")
                
# Read from stdin and process operations
if __name__ == "__main__":
    n = int(input().strip())  # Reads the number of operations
    operations = [input().strip() for _ in range(n)]
    perform_op(operations)
