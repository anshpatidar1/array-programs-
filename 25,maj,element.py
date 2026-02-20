def majority_element(arr):
    freq = {}
    n = len(arr)

    # count freq


    for x in arr:
        freq[x] = freq.get(x, 0) + 1



    # check which element appears more than n/2 times
    for key, value in freq.items():
        if value > n // 2:
            return key

    return None


# eg


arr = [2, 2, 1, 2, 3, 2, 2]
print(majority_element(arr))   