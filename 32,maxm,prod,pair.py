def max_product_pair(arr):
    arr.sort()
    return max(arr[0]*arr[1], arr[-1]*arr[-2])



#eg

print(max_product_pair([1,10,2,6,5,3]))

