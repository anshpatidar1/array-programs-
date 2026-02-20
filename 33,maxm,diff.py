def max_diff(arr):
    min_val = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_val)
        min_val = min(min_val, arr[i])
    return max_diff

print( max_diff([2,3,10,6,4,8,1]))