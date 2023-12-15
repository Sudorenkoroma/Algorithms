class Solution:
    def plusOne(self, nums: list[int]) -> int:
        index = len(nums)-1
        while nums[index] == 9 and index >= 0:
            nums[index] = 0
            index -= 1
        if index == -1:
            nums[0] = 1
            nums.append(0)
        else:
            nums[index] += 1

        return nums


nums = [1,9,9,9,9]
res = Solution()
sol = res.plusOne(nums)
print(sol)

