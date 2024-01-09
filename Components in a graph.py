def find(parent, i):
    # Find the root of the set in which element i is present
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, size, x, y):
    # Find the root of the sets in which elements x and y are present
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    # Union the two sets based on the size of the component
    if xroot != yroot:
        if size[xroot] < size[yroot]:
            parent[xroot] = yroot
            size[yroot] += size[xroot]
        else:
            parent[yroot] = xroot
            size[xroot] += size[yroot]

def componentsInGraph(gb):
    max_node = max(max(edge) for edge in gb)
    parent = {i: i for i in range(1, max_node + 1)}
    size = {i: 1 for i in range(1, max_node + 1)}
    
    for x, y in gb:
        union(parent, size, x, y)
    
    component_sizes = [size[find(parent, i)] for i in range(1, max_node + 1)]
    
    # Filter out the size of 1, since we don't consider them as components
    component_sizes = [s for s in component_sizes if s > 1]
    
    if not component_sizes:  # If there are no components, return [0, 0]
        return [0, 0]
    
    return [min(component_sizes), max(component_sizes)]



