# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

def heap_operations(queries):
    heap = []
    deleted = set()
    for query in queries:
        q_type, *values = query
        if q_type == 1:
            heapq.heappush(heap, values[0])
        elif q_type == 2:
            deleted.add(values[0])
        elif q_type == 3:
            while heap[0] in deleted:
                heapq.heappop(heap)
            print(heap[0])

# Reading input
if __name__ == "__main__":
    Q = int(input())  # Number of queries
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))

    heap_operations(queries)
