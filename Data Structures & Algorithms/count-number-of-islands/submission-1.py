class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for dx, dy in dirs:
                dfs(i+dx, j+dy)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res

            