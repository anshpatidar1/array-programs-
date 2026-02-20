def first_mis_pos(arr):
    s = set(arr)
    i = 1
    while i in s:
        i += 1
    return i



#eg
print(first_mis_pos([3,4,-1,1]))
