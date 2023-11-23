class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0

        # Iterate through the array with the fast pointer
        for fast in range(1, len(nums)):
            print(f"for {nums[slow]} = {nums[fast]}")
            # If the current element is not equal to the previous one, move the slow pointer
            if nums[fast] != nums[slow]:
                print(f"if  {nums[slow]} = {nums[fast]}")
                slow += 1
                # Copy the unique element to the next available position
                nums[slow] = nums[fast]

        # The length of the unique elements is given by the slow pointer + 1
        return print(f"R   {nums[slow]} = {nums[fast]}"), slow + 1


nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
solution.removeDuplicates(nums)
print(nums)

