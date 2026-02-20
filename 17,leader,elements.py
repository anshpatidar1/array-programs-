def leaders(arr):
    max_from_right = arr[-1]
    res = [max_from_right]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            res.append(arr[i])
    return res[::-1]




#eg
print( leaders([16,17,4,3,5,2]))
