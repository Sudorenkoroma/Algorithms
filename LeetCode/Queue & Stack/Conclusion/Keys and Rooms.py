class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)

        return len(visited) == n

rooms = [[1,3],[3,0,1],[2],[2,4],[1]]
sol = Solution()
res = sol.canVisitAllRooms(rooms)
print(res)