def minimumBribes(q):
    bribes = 0
    #  n = len(q)
    #  for i in range(n): (without reversing, longer but easier to read)
 
    """ for i in reversed(range(len(q))):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
             
        for j in range(max(0, q[i] - 2, i)):
            if q[j] > q[i]:
                bribes += 1
    
    print(bribes)
    """
    
    bribes = 0
    min_seen = float('inf')

    for i in reversed(range(len(q))):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return

        min_seen = min(min_seen, q[i])
        
        if q[i] > i + 1:
            bribes += q[i] - (i + 1)
        else:
            if min_seen < q[i]:
                bribes += 1

    print(bribes)