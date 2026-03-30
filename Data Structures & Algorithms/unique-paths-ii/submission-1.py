class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        def dfs(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0

            elif (i, j) == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                return 1
            
            elif dp[i][j] != -1:
                return dp[i][j]
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)

            res = down + right
            dp[i][j] = res
            return res

        return dfs(0, 0)

