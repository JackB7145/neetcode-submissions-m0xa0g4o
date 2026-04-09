class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0

            elif (i, j) == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                return 1
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)

            return down + right

        return dfs(0, 0)

