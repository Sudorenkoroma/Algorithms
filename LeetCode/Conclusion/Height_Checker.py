class Solution:
    def heightChecker(self, nums):
        nums_sort = sorted(nums)
        k = 0
        for i in range(len(nums)):
            if nums_sort[i] != nums[i]:
                k += 1

        return k


array = [1,1,4,2,1,3]

res = Solution()
result = res.heightChecker(array)
print(result)
