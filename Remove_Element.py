class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Змінна для відстеження нової довжини масиву

        # Ітеруємося по елементах масиву
        for i in range(len(nums)):
            if nums[i] != val:
                # Якщо елемент не дорівнює val, то збільшуємо k та записуємо елемент на нову позицію
                nums[k] = nums[i]
                # print(nums)
                k += 1
        nums[:] = nums[:k]
        return k, nums

# Приклад виклику функції
nums = [3,2,2,3]
val = 3
solution = Solution()
result, modified_nums = solution.removeElement(nums, val)
print(result, modified_nums)
