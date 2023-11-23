
test = {
    'input1': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []

tests.append(test)

tests.append({
    'input2': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input3': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last element
tests.append({
    'input4': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input5': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})
# cards does not contain query
tests.append({
    'input6': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards is empty
tests.append({
    'input7': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards
tests.append({
    'input8': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# query occurs multiple times
tests.append({
    'input9': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


def locate_card(cards, query):

    def binary_search(lo, hi, condition):

        while lo <= hi:
            mid = (lo + hi) // 2
            result = condition(mid)
            if result == 'found':
                return mid
            elif result == 'left':
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    # def first_position(nums, target):
    #     def condition(mid):
    #         if nums[mid] == target:
    #             if mid > 0 and nums[mid - 1] == target:
    #                 return 'left'
    #             return 'found'
    #         elif nums[mid] < target:
    #             return 'right'
    #         else:
    #             return 'left'
    #
    #     return binary_search(0, len(nums) - 1, condition)
    #
    # def last_position(nums, target):
    #     def condition(mid):
    #         if nums[mid] == target:
    #             if mid < len(nums) - 1 and nums[mid + 1] == target:
    #                 return 'right'
    #             return 'found'
    #         elif nums[mid] < target:
    #             return 'right'
    #         else:
    #             return 'left'
    #
    #     return binary_search(0, len(nums) - 1, condition)
    #
    # def first_and_last_position(nums, target):
    #     return first_position(nums, target), last_position(nums, target)

    return binary_search(0, len(cards) - 1, condition)\



i = 0
for i in range(9):
    result = locate_card(tests[i][f'input{i+1}']['cards'], tests[i][f'input{i+1}']['query'])
    res = tests[i]['output'] == result
    print(f"TestN {i+1} is {res}. {result}")
