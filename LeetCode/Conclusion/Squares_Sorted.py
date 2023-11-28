class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = num ** 2
            res.append(num)
            res.sort()

        return res

nums = [-4,-1,0,3,10]


solution = Solution()
resolt = solution.sortedSquares(nums)
print(resolt)