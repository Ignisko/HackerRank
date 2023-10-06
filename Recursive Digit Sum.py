def superDigit(n, k):
    def calculate_super_digit(n):
        if len(n) == 1:
            return n
        total = sum(map(int, n))
        return calculate_super_digit(str(total))

    initial_super_digit = calculate_super_digit(n)
    final_super_digit = int(initial_super_digit) * k

    return calculate_super_digit(str(final_super_digit))
