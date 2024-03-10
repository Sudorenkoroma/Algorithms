class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}
        def dfs (index,count):
            if index == len(nums):
                if count == target:
                    return 1
                else:
                    return 0
            if (index, count) in dp:
                return dp [(index, count)]
            dp[(index, count)] = dfs(index+1, count + nums[index]) + dfs(index+1, count - nums[index])

            return dp[(index, count)]

        return dfs(0,0)



nums = [1,1,1,1,1]
target = 3
sol = Solution()
res = sol.findTargetSumWays(nums, target)
print(res)