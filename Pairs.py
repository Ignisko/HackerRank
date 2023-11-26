def pairs(k, arr):
    unique_elements = set()
    pair_count = 0
    
    for number in arr:
        if (number + k) in unique_elements:
            pair_count += 1
        if (number - k) in unique_elements:
            pair_count += 1
        unique_elements.add(number)
        
    return pair_count

# Usage example:
arr = [1, 2, 3, 4]
k = 1
print(pairs(k, arr))  # Output should be 3
