def detonate(grid):
    r, c = len(grid), len(grid[0])
    new_grid = [['O'] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "O":
                new_grid[i][j] = "."
                if i > 0:
                    new_grid[i-1][j]= "."
                if i < r-1:
                    new_grid[i+1][j] = "."
                if j > 0:
                    new_grid[i][j-1] = "."
                if j < c-1:
                    new_grid[i][j+1]= "."
    return ["".join(row) for row in new_grid]
    
    
def bomberMan(n, grid):
    if n == 1:
        return grid
        
    state1 = detonate(grid)
    state2 = detonate(state2)
    
    if n % 4 == 1:
        return state2
    if n % 2 == 0:
        return ['O' * len(grid[0]) for _ in grid]
    if n % 4 == 3:
        return state1
