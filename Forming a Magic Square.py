def getCost(arr, magic):
    return sum(abs(arr[i][j] - magic[i][j]) for i in range(3) for j in range(3))

def formingMagicSquare(s):
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    ]

    minCost = float('inf')
    for square in magic_squares:
        cost = getCost(square, s)
        minCost = min(minCost, cost)
    return minCost