class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

def mergeCommunities(n, queries):
    disjoint_set = DisjointSet(n)
    result = []

    for query in queries:
        if query[0] == 'M':
            i, j = map(int, query[1:])
            disjoint_set.union(i, j)
        elif query[0] == 'Q':
            i = int(query[1])
            result.append(disjoint_set.size[disjoint_set.find(i)])

    return result

# Read input
n, q = map(int, input().split())
queries = [input().split() for _ in range(q)]

# Get the output
output = mergeCommunities(n, queries)
for res in output:
    print(res)
