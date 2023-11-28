class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Позначте індекси відповідних чисел, як від'ємні
        for num in nums:
            print(f"{abs(num)-1} = abs({num})-1")
            index = abs(num) - 1
            print(f"{nums}, {nums[index]} = {-abs(nums[index])}")
            nums[index] = -abs(nums[index])
            print(f"{nums}")
            print("______________________")


        # Зберіть всі невід'ємні індекси + 1
        result = [i + 1 for i in range(n) if nums[i] > 0]

        return result


array = [4,3,2,7,8,2,3,1]

res = Solution()
result = res.findDisappearedNumbers(array)
print(result)