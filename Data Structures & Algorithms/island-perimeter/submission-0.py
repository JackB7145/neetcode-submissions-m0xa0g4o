class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        dfs algorithm with a postorder cleaning stage. 

        we return 1 + left + right+ up + down

        but for every direction == 0, we don't just do 1, we do 4 - how many times these directions were something other than 0. 
        '''
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
                return 0
            
            value = 4 if (i, j) == (0, 0) else 3

            visited.add((i, j))

            left = dfs(i-1, j)
            right = dfs(i+1, j)
            up = dfs(i, j-1)
            down = dfs(i, j+1)

            visited.remove((i, j))

            for x in [left, right, up, down]:
                if x != 0:
                    value -= 1
            
            return value + left + right + up + down
        
        return dfs(0, 0)

