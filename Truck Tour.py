Truck Tour
def truckTour(petrolpumps):
    start_point = 0
    total_petrol = 0
    total_distance = 0

    for i in range(len(petrolpumps)):
        total_petrol += petrolpumps[i][0]
        total_distance += petrolpumps[i][1]

        if total_petrol < total_distance:
            start_point = i + 1
            total_petrol = 0
            total_distance = 0

    return start_point

# Example usage:
petrolpumps = [[1, 5], [10, 3], [3, 4]]
print(truckTour(petrolpumps))
