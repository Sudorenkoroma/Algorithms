class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = []
        rowIndex += 1
        for i in range(1, rowIndex + 1):
            pascal.append([1] * i)
            if len(pascal[i - 1]) >= 3:
                for j in range(1, len(pascal[i - 1]) - 1):
                    pascal[i - 1][j] = pascal[i - 2][j - 1] + pascal[i - 2][j]

        return pascal[rowIndex-1]


rowIndex = 3
res = Solution()
result = res.getRow(rowIndex)
print(result)