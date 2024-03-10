from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        remade = [[float("inf")]*col for _ in range(row)]
        queue = deque()
        dimention = [(0,1),(0,-1),(-1,0),(1,0)]
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    remade[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for x, y in dimention:
                new_r, new_c = x+r, y+c
                if 0 <= new_r <= row-1 and 0 <= new_c <= col-1:
                    if remade[new_r][new_c] > remade[r][c]:
                        remade[new_r][new_c] = remade[r][c] + 1
                        queue.append((new_r, new_c))

        return remade


mat = [[0,0,1],[0,1,1],[1,1,1]]

res = Solution()
sol = res.updateMatrix(mat)
print(sol)