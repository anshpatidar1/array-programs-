def move_zeroes(arr):
    non_zero = [x for x in arr if x != 0]
    return non_zero + [0]*(len(arr)-len(non_zero))




#eg


print( move_zeroes([0,1,0,3,12]))
