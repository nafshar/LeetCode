def threeSum(nums):
    if (len(nums) <= 3):
        return []
    nums.sort()
    result, sum, i = [], 0, 0
    for i in range(len(nums) - 3):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if (nums[i] != nums[left] and \
                    nums[i] != nums[right] and \
                    nums[left] != nums[right]):
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.add([nums[i], nums[left], nums[right]])
                    left, right = i + 1, right - 1
                elif sum < 0:
                    left += 1
                else:
                    return result
            if(nums[i] == nums[left] or nums[left] == nums[right]): i += 1
            if(nums[i] == nums[right]): right -= 1


ar = [-1,0,1,2,-1,-4]
rs = threeSum(ar)
print(rs)