def counterGame(n):
    # Count the number of set bits in n - 1
    count = bin(n - 1).count('1')
    
    # If the count is even, Richard wins; otherwise, Louise wins
    return "Richard" if count % 2 == 0 else "Louise"

def whoWinsGame(testcases):
    results = []
    for n in testcases:
        winner = counterGame(n)
        results.append(winner)
    return results

        