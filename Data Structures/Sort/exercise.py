def shell_sort(arr):
    size = len(arr)
    gap = size//2
    index_count = []

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
            if arr[j] == arr[j-1]:
                index_count.append(j-1)
        gap = gap // 2
    for i in range(len(arr)-1,-1,-1):
        if index_count and i == index_count[-1]:
            arr.pop(i)
            index_count.pop()


elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
shell_sort(elements)
print(elements)
