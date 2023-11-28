large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}


def locate_card(cards, query):     # must add first_and_last_position


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

    return binary_search(0, len(cards) - 1, condition)




result = locate_card(large_test['input']['cards'], large_test['input']['query'])
print("Result:", result)


