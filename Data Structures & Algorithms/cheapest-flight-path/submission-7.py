import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # (cost, stops, node)
        heap = [(0, 0, src)]
        
        # Track best cost to reach (node with <= stops)
        best = dict()  # (node, stops) -> cost
        
        while heap:
            cost, stops, node = heapq.heappop(heap)
            
            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            # If we've already seen a better state, skip
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            
            best[(node, stops)] = cost
            
            for nei, price in adj[node]:
                heapq.heappush(heap, (cost + price, stops + 1, nei))
        
        return -1