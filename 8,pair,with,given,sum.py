#⁠Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def pair_with_sum(arr, target):
    seen = set()
    for x in arr:
        if target - x in seen:
            return (x, target - x)
        seen.add(x)
    return None




#eg
print( pair_with_sum([2,7,11,15], 9))
