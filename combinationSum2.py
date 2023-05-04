def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    print(candidates)
    result = []
    index = -1
    for i in range(len(candidates)):
        if candidates[i] >= target:
            index = i
            break
    if index == -1: return result.append([])

    #if the left most item is already = target, then return it immediately
    if candidates[0] == target:
        result.append([candidates[0]])
        return result

    # index is as far as we need to look in the list
    rptr = index
    lptr = 0
    idx = []
    while lptr < rptr:
        if(candidates[rptr] == target):
            result.append([candidates[rptr]])
            rptr -= 1
            continue
        sum = candidates[rptr]
        idx.append(rptr)
        # lptr_reset = False
        for i in range(lptr, rptr):
            sum = sum + candidates[i]
            idx.append(i)
            if(sum == target):
                tmplst = []
                for j in idx:
                    tmplst.append(candidates[j])
                if tmplst not in result: result.append(tmplst)
                lptr += len(idx)-1
                idx = []
                idx.append(rptr)
                sum = candidates[rptr]
        idx = []
        lptr = 0
        rptr -= 1



    return result


# ar = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# ar = [2,5,2,1,2]
# target = 5
ar = [3,3,3]
target = 3
lst = combinationSum2(ar, target)
print(lst)
