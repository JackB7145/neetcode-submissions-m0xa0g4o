import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # heap ordered by start time
        heap = []
        for i, (start, proc) in enumerate(tasks):
            heapq.heappush(heap, (start, proc, i))
        
        backlog = []  # ordered by (processing_time, index)
        res = []
        
        seconds = 0
        cooldown = 0
        
        while heap or backlog or cooldown > 0:
            
            # If CPU is idle and nothing ready, jump time forward
            if cooldown == 0 and not backlog and heap:
                seconds = max(seconds, heap[0][0])
            
            # Move tasks that have arrived into backlog
            while heap and heap[0][0] <= seconds:
                start, proc, idx = heapq.heappop(heap)
                heapq.heappush(backlog, (proc, idx))
            
            # If CPU is idle and something is ready
            if cooldown == 0 and backlog:
                proc, idx = heapq.heappop(backlog)
                res.append(idx)
                cooldown = proc
            
            # Advance time if CPU working
            if cooldown > 0:
                seconds += 1
                cooldown -= 1
        
        return res