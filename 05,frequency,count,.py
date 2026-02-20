#5.⁠ ⁠Count Frequency of Elements


def frequency(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq





# for an eg

print( frequency([1,2,2,3,1,1]))

