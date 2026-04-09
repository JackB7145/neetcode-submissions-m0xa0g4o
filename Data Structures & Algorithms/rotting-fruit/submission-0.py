class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Count the number of rotting fruits originally in the search for the total
        add onto a queue the rotten ones, subtracting each from the total when we trun a good orange into
        a rotton orange
        return what's left
        '''

        count = 0 
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    count += 1
        visited = set()
        minute = -1
        while queue:
            minute+=1
            print('New Minute: ', minute)
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
                    continue
                
                print(i, j)
                count -= 1
                grid[i][j] = 2
                visited.add((i, j))
                queue.append((i+1, j))
                queue.append((i-1, j))
                queue.append((i, j-1))
                queue.append((i, j+1))

        if count != 0:
            return -1
        return minute-1            

