class Solution:
    def sortArrayByParity(self, nums: list[int]) -> None:
        if not nums:
            return []

        # Вказівник для зберігання позиції, на якій ми можемо розмістити наступний парний елемент
        Parity_index = 0

        # Проходимося по масиву
        for i in range(len(nums)):
            # Якщо поточний елемент є парним
            if nums[i] % 2 == 0:
                # Міняємо його з першим парним елементом або залишаємо на місці, якщо всі парні вже були відсунуті
                nums[i], nums[Parity_index] = nums[Parity_index], nums[i]
                # Збільшуємо вказівник для парних елементів
                Parity_index += 1

        return nums


nums = [3,1,2,4]
res = Solution()
resolt = res.sortArrayByParity(nums)
print(resolt)