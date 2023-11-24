class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return []

            # Вказівник для зберігання унікальних елементів
        unique_pointer = 0

        # Ітерація по масиву для видалення дублікатів
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pointer]:
                unique_pointer += 1
                nums[unique_pointer] = nums[i]

        # Повертаємо унікальні елементи, знаходячися в межах вказівника
        return nums[:unique_pointer + 1]


array = [0, 0, 1, 1, 2, 2, 3, 4]
Output: [0, 1, 2, 3, 4]

res = Solution()
resolt = res.removeDuplicates(array)
print(resolt)

