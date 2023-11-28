class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        # loops = nums.count(val)
        # for i in range(loops):
        #     nums.remove(val)

        # while loops != 0:
        #     nums.remove(val)
        #     loops -= 1

        return len(nums)


nums = [0,1,1,2,2,3,4,2]
val = 2

res = Solution()
result = res.removeElement(nums, val)
print(result)
