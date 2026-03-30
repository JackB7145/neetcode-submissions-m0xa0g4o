class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while heap and len(heap) > 1:
            val1, val2 = -heapq.heappop(heap), -heapq.heappop(heap)
            heapq.heappush(heap, -(val1-val2))
        if not heap:
            return 0
        return -heap[0]
        
            
            
