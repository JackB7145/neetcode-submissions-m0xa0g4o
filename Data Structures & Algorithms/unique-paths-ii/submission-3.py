class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "X"

        if obstacleGrid[n-1][m-1] == "X":
            return 0

        obstacleGrid[n-1][m-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if [i, j] == [n-1, m-1] or obstacleGrid[i][j] == "X":
                    continue

                val1 = obstacleGrid[i+1][j] if i < n-1 and obstacleGrid[i+1][j] != "X" else 0
                val2 = obstacleGrid[i][j+1] if j < m-1 and obstacleGrid[i][j+1] != "X" else 0

                obstacleGrid[i][j] = val1 + val2

        ans = obstacleGrid[0][0]
        return ans if ans != "X" else 0