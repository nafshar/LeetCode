from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    result = []

    def backtrack(start, comb):
        if len(comb) == k:
            result.append(comb.copy())
            return

        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()

    backtrack(1, [])
    return result



rst = combine(8, 4)
print(rst)
print (len(rst))