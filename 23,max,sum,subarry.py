def max_subarray(arr):
    max_sum = curr = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        max_sum = max(max_sum, curr)
    return max_sum





#eg
print( max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
