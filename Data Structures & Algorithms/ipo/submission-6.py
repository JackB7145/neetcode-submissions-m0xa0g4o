import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap based on capital required
        minHeap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(minHeap)

        # Max-heap for profits (store negative for max behavior)
        maxHeap = []

        for _ in range(k):
            # Add all projects we can afford
            while minHeap and minHeap[0][0] <= w:
                cap, prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -prof)

            # If nothing available, stop early
            if not maxHeap:
                break

            # Take the most profitable project
            w += -heapq.heappop(maxHeap)

        return w