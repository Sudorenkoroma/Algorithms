from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Create a result matrix initialized with maximum possible values
        result = [[float('inf')] * cols for _ in range(rows)]

        # Create a queue for BFS
        queue = deque()

        # Initialize the queue with 0s and mark them as visited
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))

        # Perform BFS to find the nearest 0 for each cell
        while queue:
            x, y = queue.popleft()

            # Explore the four possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                # Check if the new coordinates are within bounds
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    # If the current distance is greater than the new distance + 1
                    if result[new_x][new_y] > result[x][y] + 1:
                        result[new_x][new_y] = result[x][y] + 1
                        queue.append((new_x, new_y))

        return result


mat = [[0,0,0],[0,1,0],[1,1,1]]

res = Solution()
sol = res.updateMatrix(mat)
print(sol)