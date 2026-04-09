class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stones = reversed(stones)
        heap = []
        for stone in stones:
            heapq.heappush(heap, stone)
            if len(heap) == 2:
                val1, val2 = heap.pop(), heap.pop()
                heap.append(val1-val2)
        if heap:
            return heap[0]
        return 0
            
                

            
            
