def sumXor(n):
    if n == 0:
        return 1  # Special case: 0 + 0 = 0 ^ 0 = 0, so there is one satisfying value (x=0)

    count = 0
    while n > 0:
        if n % 2 == 0:
            count += 1
        n //= 2

    return 2 ** count
