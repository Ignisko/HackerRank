import sys

def floyd_warshall(road_nodes, road_edges, queries):
    for itr in range(road_nodes):
        for x in range(road_nodes):
            for y in range(road_nodes):
                if road_edges[x][itr] + road_edges[itr][y] <= road_edges[x][y] and (road_edges[x][itr] != sys.maxsize or road_edges[itr][y] != sys.maxsize):
                    road_edges[x][y] = road_edges[x][itr] + road_edges[itr][y]
    
    results = []
    for x, y in queries:
        x -= 1
        y -= 1
        if road_edges[x][y] == sys.maxsize:
            results.append('-1')
        else:
            results.append(str(road_edges[x][y]))
    
    return results

if __name__ == '__main__':
    road_nodes, num_road_edges = map(int, input().split())
    
    road_edges = [[sys.maxsize for _ in range(road_nodes)] for _ in range(road_nodes)]
    for l in range(road_nodes):
        road_edges[l][l] = 0
    
    for road_itr in range(num_road_edges):
        road_from, road_to, road_weight = map(int, input().split())
        road_from -= 1
        road_to -= 1
        road_edges[road_from][road_to] = road_weight
    
    queries = []
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        queries.append((x, y))

    results = floyd_warshall(road_nodes, road_edges, queries)
    for result in results:
        print(result)
