class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # End Condition: left > right
        return -1

nums = [4,5,6,7,8,9,0,1,2]
target = 1
sol = Solution()
res = sol.search(nums, target)
print(res)