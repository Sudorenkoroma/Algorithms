class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = {}

        def dfs(index, total):
            if index == len(nums) - 1:
                if total == target:
                    return 1
                else:
                    return 0
            if (index, total) in dp:
                return dp[(index, total)]
            dp[(index, total)] = dfs(index + 1, total + nums[index + 1]) + dfs(index + 1, total - nums[index + 1])
            return dp[(index, total)]

        return dfs(-1, 0)


nums = [1,1,1,1,1]
target = 33
sol = Solution()
res = sol.findTargetSumWays(nums, target)
print(res)
