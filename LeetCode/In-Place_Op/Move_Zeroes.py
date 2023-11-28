class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if not nums:
            return []

        # Вказівник для зберігання позиції, на якій ми можемо розмістити наступний ненульовий елемент
        non_zero_index = 0

        # Проходимося по масиву
        for i in range(len(nums)):
            # Якщо поточний елемент не є нулем
            if nums[i] != 0:
                # Міняємо його з першим нульовим елементом або залишаємо на місці, якщо всі нулі вже були відсунуті
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Збільшуємо вказівник для ненульових елементів
                non_zero_index += 1

        return nums


nums = [0,1,0,3,3,12,0]
res = Solution()
resolt = res.moveZeroes(nums)
print(resolt)

