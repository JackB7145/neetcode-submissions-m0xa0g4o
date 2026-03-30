
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            heapq.heappush(heap, ((points[i][0]**2 + points[i][1]**2)**0.5, points[i]))
        
        for i in range(k):  
            res.append(heapq.heappop(heap)[1])

        return res
        


