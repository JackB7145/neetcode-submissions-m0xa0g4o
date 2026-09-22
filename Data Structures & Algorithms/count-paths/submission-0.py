class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        grid[-1][-1] = 1

        print(grid)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                bottom = grid[i+1][j] if i < n - 1 else 0
                right = grid[i][j+1] if j < m - 1 else 0
                print(bottom, right)

                grid[i][j] = bottom + right
        
        return grid[0][0]