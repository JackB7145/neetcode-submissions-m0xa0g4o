class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(i, j):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            traverse(i-1, j)
            traverse(i+1, j)
            traverse(i, j-1)
            traverse(i, j+1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    traverse(i, j)
                    res += 1
                
        return res