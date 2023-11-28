nums = [4,3,2,7,8,2,3,1]
for num in nums:
    index = abs(num) - 1
    print(f"i{index},nums[i]{nums[index]}")
    nums[index] = -abs(nums[index])
print(nums)