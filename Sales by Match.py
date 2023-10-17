def count_pairs(ar):
    """
    Count the number of pairs in a given list 'ar'.

    Parameters:
    - ar (list): The list of integers.

    Returns:
    - int: The number of pairs.
    """
    count_pairs = 0  # Initialize the count of pairs
    ar.sort()  # Sort the array for easier pair matching

    i = 0  # Initialize the index
    n = len(ar)  # Get the length of the array

    while i < (n - 1):
        # Check if a valid pair is found
        if ar[i] == ar[i + 1]:
            count_pairs += 1  # Increment the pair count
            i += 2  # Skip the elements of the current pair
        else:
            i += 1  # Move to the next element

    return count_pairs  # Return the total number of pairs