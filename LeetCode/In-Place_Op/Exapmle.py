def square_even(array):
    # Перевірка на крайовий випадок.
    if array is None:
        return array

    # Ітеруємося по вихідному масиву.
    for i in range(len(array)):
        # Якщо індекс парний, ми повинні підняти елемент у квадрат
        # і замінити оригінальне значення в масиві.
        if i % 2 == 0:
            array[i] *= array[i]
        # Зверніть увагу, що нам не потрібно *нічого* робити для непарних індексів. :-)

    # Просто повертаємо оригінальний масив. У деяких задачах на LeetCode вимагається його повернення, а в інших - ні.
    return array

original_array = [1, 2, 3, 4, 5]
result_array = square_even(original_array, len(original_array))
print(result_array)

