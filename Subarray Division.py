# Define a function named 'birthday' that takes three parameters: s (the chocolate bar), d (Ron's birth day), and m (Ron's birth month)
def birthday(s, d, m):
    count = 0  # Initialize a variable to keep track of the number of ways to divide the chocolate bar

    # Iterate over the chocolate bar from the first square to the (n - m) square, where n is the length of the chocolate bar
    for i in range(len(s) - m + 1):
        # Extract a segment of the chocolate bar with a length of m, starting from position i
        segment = s[i:i + m]

        # Check if the sum of the integers in the segment is equal to Ron's birth day
        if sum(segment) == d:
            count += 1  # If it is, increment the count

    return count  # Return the total count of valid segments

# Example usage:
# Input parameters: s=[1, 2, 1, 3, 2], d=3, m=2
# Function call: birthday(s, d, m)
# Output: 2