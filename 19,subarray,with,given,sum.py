def subarray_with_sum(arr, target):
    curr = 0
    start = 0
    for i in range(len(arr)):
        curr += arr[i]
        while curr > target:
            curr -= arr[start]
            start += 1
        if curr == target:
            return arr[start:i+1]
    return None




#eg

print( subarray_with_sum([1,2,3,7,5], 12))
