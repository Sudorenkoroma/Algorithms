def generate_pascals_triangle(numRows):
    pascal = []
    for i in range(1, numRows +1):
        pascal.append([1] * i)
        if len(pascal[i-1]) >= 3:
            for j in range(1,len(pascal[i-1])-1):
                pascal[i-1][j] = pascal[i-2][j-1] + pascal[i-2][j]

    return pascal

# Example usage:
numRows = 2
result = generate_pascals_triangle(numRows)

# for row in result:
#     print(row)
print(result)
# fvoizdfhvidh