class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue

                curr = grid[i][j]

                down = grid[i + 1][j] if i + 1 < n else float("inf")
                right = grid[i][j + 1] if j + 1 < m else float("inf")

                grid[i][j] = curr + min(down, right)

        return grid[0][0]
