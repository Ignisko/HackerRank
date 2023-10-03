def gamingArray(arr):
    mx = 0
    count = 0

    for x in arr:
        if x > mx:
            mx = x
            count += 1

    if count % 2 == 0:
        return "ANDY"
    else:
        return "BOB"