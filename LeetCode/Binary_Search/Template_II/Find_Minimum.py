class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# nums = [8,9,1,2,3,4,5,6,7]
nums = [3,4,5,1,2]
sol = Solution()
res = sol.findMin(nums)
print(res)