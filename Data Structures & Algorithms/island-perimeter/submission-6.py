class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def traverse(i, j):
            nonlocal res
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0 

            if (i, j) in seen:
                return 0 if grid[i][j] == 0 else 1
                
            seen.add((i, j))
            perimeter = 4
            for dx, dy in dirs:
                perimeter -= traverse(i+dx, j+dy)
            
            res += perimeter
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen:
                    traverse(i, j)
        
        return res