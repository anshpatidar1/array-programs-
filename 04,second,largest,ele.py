#Find the Second Largest Element
def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]



# for an eg

print( second_largest([10,5,20,8])) 
