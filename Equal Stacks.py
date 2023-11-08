Equal Stacks

def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)

    # Use index pointers for the stacks
    index1, index2, index3 = 0, 0, 0

    while not (sum1 == sum2 == sum3):
        # Find the stack with the largest sum and remove the top element from it
        if sum1 >= sum2 and sum1 >= sum3 and index1 < len(h1):
            sum1 -= h1[index1]
            index1 += 1
        elif sum2 >= sum1 and sum2 >= sum3 and index2 < len(h2):
            sum2 -= h2[index2]
            index2 += 1
        elif index3 < len(h3):
            sum3 -= h3[index3]
            index3 += 1

        # In the case where any stack becomes empty
        if index1 == len(h1) or index2 == len(h2) or index3 == len(h3):
            return 0

    return sum3  # At this point, sum1 == sum2 == sum3 so we can return any
