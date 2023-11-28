class Solution:
    def search(self, nums: list[int], target: int) -> int:
    # _position
        def binary_search(lo, hi, condition):

            while lo <= hi:
                mid = (lo + hi) // 2
                result = condition(mid)
                if result == 'found':
                    return mid
                elif result == 'left':
                    hi = mid - 1
                else:
                    lo = mid + 1
            return "not found"

        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    return 'left'
                else:
                    return 'found'
            elif nums[mid] > target:
                return 'left'
            else:
                return 'right'

        return binary_search(0, len(nums) - 1, condition)


nums = [-1,0,3,5,9,12]
target = 9

solution = Solution()
res = solution.search(nums, target)
print(res)
