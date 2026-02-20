def all_subarrays(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            res.append(arr[i:j+1])
    return res



#eg

print( all_subarrays([1,2]))