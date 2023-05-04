def tsc (nums, target) :
    if (len(nums) <= 3):
        return sum(nums)
    nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i - 1]:
            j, k = i + 1, len(nums) - 1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    j += 1
                elif diff > 0:
                    k -= 1
                else:
                    return target
        i += 1
    return result

ar = [4,0,5,-5,3,3,0,-4,-5]
target = -2
sm = tsc(ar, target)
print ("closest_sum = ", sm)