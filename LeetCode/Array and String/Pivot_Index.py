def pivotIndex(nums):
    for i in range(0, len(nums)):
        sum_left = sum(nums[:i])
        sum_right = sum(nums[i+1:])
        if sum_left == sum_right:
            return i

    return -1


nums = [1,7,3,6,5,6]
res = pivotIndex(nums)
print(res)