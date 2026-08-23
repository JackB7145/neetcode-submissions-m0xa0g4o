class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            cnt = 1
            for dx, dy in dirs:
                cnt += dfs(i+dx, j+dy)

            return cnt

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res