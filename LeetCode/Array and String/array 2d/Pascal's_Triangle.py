def generate_pascals_triangle(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

# Example usage:
numRows = 5
result = generate_pascals_triangle(numRows)

for row in result:
    print(row)

# fvoizdfhvidh