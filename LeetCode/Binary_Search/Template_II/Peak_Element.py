class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        # End Condition: left > right
        return left


nums = [1,2,1,3,5,6,4]
sol = Solution()
res = sol.findPeakElement(nums)
print(res)


