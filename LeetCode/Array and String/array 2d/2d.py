class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        while matrix:
            # Traverse top row
            result += matrix.pop(0)

            # Traverse right column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Traverse bottom row in reverse order
            if matrix and matrix[0]:
                result += matrix.pop()[::-1]

            # Traverse left column in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result


mat = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution()
sol = res.spiralOrder(mat)

print(sol)