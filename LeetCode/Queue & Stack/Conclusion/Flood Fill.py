class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int):
        grid = image
        rows = len(grid)
        cols = len(grid[0])
        change_color = grid[sr][sc]

        def dig(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == change_color and grid[row][col] != color:
                grid[row][col] = color
                dig(row-1, col)
                dig(row+1, col)
                dig(row, col-1)
                dig(row, col+1)



        dig(sr, sc)
        return grid

image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2
res = Solution()
sol = res.floodFill(image, sr, sc, color)
print(sol)