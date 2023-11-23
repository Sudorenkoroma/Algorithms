import time

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}

def locate_card_linear(cards, query):
    position = 0
    start_time = time.time()
    while position < len(cards):
        if cards[position] == query:
            end_time = time.time()  # Кінець вимірювання часу
            elapsed_time = end_time - start_time
            return position, elapsed_time
        position += 1
    end_time = time.time()  # Кінець вимірювання часу, якщо число не знайдено
    elapsed_time = end_time - start_time
    return -1, elapsed_time

def test_location(cards, query, mid):
    mid_number = cards[mid]
    # print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    start_time = time.time()

    while lo <= hi:
        # print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            end_time = time.time()  # Кінець вимірювання часу
            elapsed_time = end_time - start_time
            return mid, elapsed_time
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

    end_time = time.time()  # Кінець вимірювання часу, якщо число не знайдено
    elapsed_time = end_time - start_time
    return -1, elapsed_time


result, elapsed_time = locate_card(large_test['input']['cards'], large_test['input']['query'])
print("Result:", result)
print("Passed:", result == large_test['output'])
print("Execution Time:", elapsed_time, "seconds")

line_res, elapsed_line = locate_card_linear(large_test['input']['cards'], large_test['input']['query'])
print("Result:", line_res)
print("Passed:", line_res == large_test['output'])
print("Execution Time:", elapsed_line, "seconds")