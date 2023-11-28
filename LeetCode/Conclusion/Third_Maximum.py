class Solution:
    def thirdMax(self, nums):
        if not nums:
            return []
        unique_nums = set(nums)

        # Перевірка, чи є в массиві достатньо елементів для знаходження третього максимуму.
        if len(unique_nums) < 3:
            # Якщо немає третього максимуму, повертаємо максимальний елемент.
            return max(unique_nums)

        # Використовуємо вбудовану функцію sorted() для сортування унікальних значень в порядку спадання.
        sorted_unique_nums = sorted(unique_nums, reverse=True)

        # Повертаємо третє максимальне значення.
        return sorted_unique_nums[2]


array = [1, 4, 4, 3]
res = Solution()
result = res.thirdMax(array)
print(result)