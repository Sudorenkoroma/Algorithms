class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m = max(nums)
        index = nums.index(m)
        for i in range(0, len(nums)):
            if nums[i]*2 > m and nums[i] != m:
                return -1

        return index


nums = [3,6,1,0]
res = Solution()
sol = res.dominantIndex(nums)
print(sol)