def maxima(number):
    x = number[0]
    for num in number:
        if x < num:
            x = num
    return x
