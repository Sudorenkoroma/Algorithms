# def bubble_sort(element):
#     size = len(element)
#
#     for k in range(size-1):
#         swapped = False
#         for i in range(size - 1 - k):
#             if element[i] > element[i+1]:
#                 tmp = element[i]
#                 element[i] = elements[i+1]
#                 element[i+1] = tmp
#                 swapped =True
#         if not swapped:
#             break
#
#
#
# if __name__ == "__main__":
#     elements = [5, 9, 2, 1, 67, 34, 88, 34]
#
#     bubble_sort(elements)
#     print(elements)

def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
    print(elements)