def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]



#eg

print( rotate_left([1,2,3,4,5], 2))
