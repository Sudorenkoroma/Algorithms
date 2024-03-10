class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def first(nums, target):
            left, right = 0, len(nums) - 1
            while left+1<right:
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            return right
        def last(nums, target):
            left, right = 0, len(nums) - 1
            while left+1<right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            return left

        first = first(nums,target)
        last = last(nums,target)
        if nums[first] == target and nums[last] == target:
            return [first, last]
        else:
            return [-1,-1]


nums = []
target = 0
sol = Solution()
res = sol.searchRange(nums, target)
print(res)