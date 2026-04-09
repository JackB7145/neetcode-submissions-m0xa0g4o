class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            print(heap)
            if len(heap) == 2:
                val1, val2 = -heapq.heappop(heap), -heapq.heappop(heap)
                heapq.heappush(heap, -(val1-val2))
            else:
                heapq.heappush(heap, -stone)
        if len(heap) == 2:
            print(heap)
            val1, val2 = -heapq.heappop(heap), -heapq.heappop(heap)
            heapq.heappush(heap, -(val1-val2))
        if not heap:
            return 0
        return -heap[0]
                

            
            
