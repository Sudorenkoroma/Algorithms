class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        direction = 1  # 1 for upwards, -1 for downwards
        i, j = 0, 0

        for _ in range(rows * cols):
            result.append(mat[i][j])

            i -= direction
            j += direction

            # Check boundaries and update direction
            if i >= rows:
                i = rows - 1
                j += 2
                direction = -direction
            elif j >= cols:
                j = cols - 1
                i += 2
                direction = -direction
            elif i < 0:
                i = 0
                direction = -direction
            elif j < 0:
                j = 0
                direction = -direction

        return result



mat = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution()
sol = res.findDiagonalOrder(mat)

print(sol)