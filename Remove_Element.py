def remove_elements(nums, val):
    k = 0  # Змінна для відстеження нової довжини масиву

    # Ітеруємося по елементах масиву
    for i in range(len(nums)):
        if nums[i] != val:
            # Якщо елемент не дорівнює val, то збільшуємо k та записуємо елемент на нову позицію
            nums[k] = nums[i]
            k += 1

    return k, nums

# Приклад виклику функції
nums = [0,1,2,2,3,0,4,2]
val = 2
result, modified_nums = remove_elements(nums, val)
print(f"Output: {result}, nums = {modified_nums}")