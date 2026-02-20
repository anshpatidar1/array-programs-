#Rotate Array by k Positions: Rotate the array to the right by k positions.

def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]


#for eg

print( rotate_right([1,2,3,4,5], 2))

