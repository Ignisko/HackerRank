def pylons(k, arr):
    '''i = 0
    plants = 0
    n = len(arr)
    
    while i<n:
        loc = min(i+k-1, n-1)
    
        while loc >= i-k+1 and arr[loc] == 0: #when don't use first while and put arr[i] here and next arr then it solves some correctly
            loc -= 1
       
        if loc < i+k-1 and arr[loc] == 0:
            return -1
    
        plants += 1
        i = loc + k
    
    return plants'''
    
    n = len(arr)
    i = 0
    plants = 0

    while i < n:
        # Try to place a plant as far to the right as possible within the range
        placed = False
        for j in range(min(i + k - 1, n - 1), i - k, -1):
            if arr[j] == 1:
                plants += 1
                i = j + k  # Move k cities forward
                placed = True
                break
        
        # If a plant was not placed within the range, return -1
        if not placed:
            return -1

    return plants
       