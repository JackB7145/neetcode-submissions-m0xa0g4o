class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)-1
        m = len(grid[0])-1

        dp = [[-1 for _ in range(len(grid))] for _ in range(len(grid[0]))]

        def dfs(i, j):
            
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')
            
            elif dp[i][j] != -1:
                return dp[i][j]

            elif i == n and j == m:
                return grid[i][j]

            total = min(dfs(i+1, j), dfs(i, j+1))
            dp[i][j] = total + grid[i][j]
            return dp[i][j]
        
        return dfs(0, 0)
