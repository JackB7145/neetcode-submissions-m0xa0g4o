class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        totalFruit = 0
        rottenFruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in [1, 2]:
                    totalFruit += 1
                    if grid[i][j] == 2:
                        queue.append((i, j))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                rottenFruit += 1
                curr = queue.popleft()
                i, j = curr

                for dx, dy in dirs:
                    newX, newY = i + dx, j + dy
                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 1:
                        queue.append((newX, newY))
                        grid[newX][newY] = 2
            
            if queue:
                minutes += 1


        for row in grid:
            print(row)
        print(rottenFruit, totalFruit)
        if rottenFruit == totalFruit:
            return minutes
        return -1
