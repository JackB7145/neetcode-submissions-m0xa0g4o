class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            # Out of bounds contributes 1 edge
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 1

            # Water contributes 1 edge
            if grid[i][j] == 0:
                return 1

            # Already visited land contributes 0
            if (i, j) in visited:
                return 0

            visited.add((i, j))

            # Sum all four directions
            return (
                dfs(i - 1, j) +
                dfs(i + 1, j) +
                dfs(i, j - 1) +
                dfs(i, j + 1)
            )

        # Start once from first land cell
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0
