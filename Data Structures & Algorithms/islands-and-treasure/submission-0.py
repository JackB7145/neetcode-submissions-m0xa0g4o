from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        # Start BFS from every treasure
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        step = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy

                    # Skip out of bounds
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                        continue

                    # Only visit unvisited rooms
                    if grid[ni][nj] != 2147483647:
                        continue

                    grid[ni][nj] = step + 1
                    queue.append((ni, nj))

            step += 1
