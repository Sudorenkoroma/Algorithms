class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        a = 0
        b = 1
        result = 0
        while b < len(nums):
            minim = min(nums[a],nums[b])
            result +=minim
            a +=2
            b +=2

        return result


nums = [1,4,3,2]
res = Solution()
sol = res.arrayPairSum(nums)
print(sol)