def rearrange_alternate(arr):
    arr.sort()
    res = []
    i, j = 0, len(arr)-1
    while i <= j:
        if i != j:
            res.append(arr[j])
            res.append(arr[i])
        else:
            res.append(arr[i])
        i += 1
        j -= 1
    return res



#eg

print( rearrange_alternate([1,2,3,4,5,6]))