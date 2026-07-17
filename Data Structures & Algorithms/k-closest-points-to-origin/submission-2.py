class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            heapq.heappush(minHeap, (math.sqrt(x**2 + y**2), x, y))

        res = []
        for _ in range(k):
            node = heapq.heappop(minHeap)
            res.append([node[1], node[2]])
        
        return res