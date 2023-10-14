def bomberMan(n, grid):
    # If n is 1, nothing happens, so return the original grid
    if n == 1:
        return grid
    
    r, c = len(grid), len(grid[0])
    
    # Function to detonate the bombs
    def detonate(old_grid):
        new_grid = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if old_grid[i][j] == 'O':
                    new_grid[i][j] = '.'
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < r and 0 <= y < c:
                            new_grid[x][y] = '.'
        return ["".join(row) for row in new_grid]