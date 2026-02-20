def find_peak(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return None



#eg
print(  find_peak([1,3,20,4,1,0]))

