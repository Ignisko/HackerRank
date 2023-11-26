def almostSorted(arr):
    sorted_arr = sorted(arr)
    
    # Check if the array is already sorted
    if arr == sorted_arr:
        print("yes")
        return

    # Find the segments where arr is not sorted
    diff = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]

    # If there's only one or two elements out of place, try swapping them
    if len(diff) == 2:
        i, j = diff
        arr[i], arr[j] = arr[j], arr[i]
        if arr == sorted_arr:
            print("yes")
            print(f"swap {i+1} {j+1}")
            return
        arr[i], arr[j] = arr[j], arr[i]  # Swap back if not successful

    # If there's a contiguous subsequence out of place, try reversing it
    elif len(diff) > 2:
        i, j = diff[0], diff[-1]
        arr[i:j+1] = arr[i:j+1][::-1]
        if arr == sorted_arr:
            print("yes")
            print(f"reverse {i+1} {j+1}")
            return
        # No need to reverse back as we've already checked

    # If neither swapping nor reversing works, print no
    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
