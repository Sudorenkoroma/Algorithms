class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dig(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] != "0":
                grid[row][col] = "0"
                dig(row-1, col)
                dig(row+1, col)
                dig(row, col-1)
                dig(row, col+1)


        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dig(r, c)


        return num_islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","1"],
  ["0","0","1","0","1"],
  ["0","0","0","1","1"]
]
res = Solution()
sol = res.numIslands(grid)
print(sol)