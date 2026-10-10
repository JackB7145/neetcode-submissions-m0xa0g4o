import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]       # (time, i, j)
        seen = {(0, 0)}

        while heap:
            t, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return t
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))