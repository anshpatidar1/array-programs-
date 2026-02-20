def remove_duplicates(arr):
    seen = set()
    res = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res




#eg
print( remove_duplicates([1,2,2,3,1]))
