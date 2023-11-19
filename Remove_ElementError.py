class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        loops = nums.count(val)

        # for i in range(loops):
        #     nums.remove(val)


        # while loops != 0:
        #     nums.remove(val)
        #     loops -= 1

        return nums


nums = [0,1,1,2,2,3,4,2]
val = 2
# print(nums)
res = Solution()
res.removeElement(nums, val)
print(nums)
