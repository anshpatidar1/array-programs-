def equilibrium_index(arr):
    total = sum(arr)
    left = 0
    for i in range(len(arr)):
        total -= arr[i]
        if left == total:
            return i
        left += arr[i]
    return -1


#eg

print( equilibrium_index([-7,1,5,2,-4,3,0]))
