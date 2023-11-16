def permutationGame(arr):
    def canWin(arr, memo):
        if tuple(arr) in memo:
            return memo[tuple(arr)]

        if arr == sorted(arr):
            # If the remaining sequence is in increasing order, the last player wins
            memo[tuple(arr)] = False
            return False

        for i in range(len(arr)):
            if not canWin(arr[:i] + arr[i + 1:], memo):
                # If removing this element leads to the opponent's losing position, current player wins
                memo[tuple(arr)] = True
                return True

        memo[tuple(arr)] = False
        return False

    memo = {}
    return "Alice" if canWin(arr, memo) else "Bob"
