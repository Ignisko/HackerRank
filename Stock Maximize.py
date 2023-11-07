Stock Maximize
#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    profit = 0
    current_max = 0
    
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] >= current_max:
            current_max = prices[i]
        else:
            profit += (current_max - prices[i])
    return profit


