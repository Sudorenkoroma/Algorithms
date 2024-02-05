class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}
        def dfs(index, current_sum):
            # Base case: if we reach the end of the array
            if index == len(nums):
                if current_sum == target:
                    return 1
                else:
                    return 0
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            # Use DFS to explore two possibilities: adding or subtracting the current number
            dp[(index, current_sum)] = dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])
            return dp[(index, current_sum)]

        return dfs(0, 0)



nums = [1,1,1,1,1]
target = 2
sol = Solution()
res = sol.findTargetSumWays(nums, target)
print(res)