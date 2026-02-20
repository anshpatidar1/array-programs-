def find_duplicates(arr):
    seen = set()
    dup = set()
    for x in arr:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)







#eg


print(find_duplicates([1,2,3,2,1,4]))
