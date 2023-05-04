from random import randint

def nextPermutation(nums):
    n = len(nums) - 1
    swap_index = n
    pivot_index = -1
    pivot = 0
    k = n
    while k > 0:
        if nums[k - 1] < nums[k]:
            pivot_index = k - 1
            pivot = nums[k - 1]
            break
        k -= 1

    # Now find a number smaller than the pivot from here forward
    if (pivot_index != -1):
        m = n
        while m > pivot_index:
            if nums[m] > pivot:
                swap_index = m
                break
            m -= 1
        # swap perm_index & smalles_index
        nums = swap(nums, pivot_index, swap_index)

    # reverse the rest after pivot index
    i = pivot_index + 1
    j = n
    while i < j:
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        i += 1
        j -= 1

    return nums


def swap(ar, i, j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp
    return ar


ar = [1,2,1,5,4,3]
# ar = [1,2,3]
# ar = [1,2]
arn = nextPermutation(ar)
print(arn)