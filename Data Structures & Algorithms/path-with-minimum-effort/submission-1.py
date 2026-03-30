import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS = len(heights)
        COLS = len(heights[0])

        dist = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        dist[0][0] = 0

        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))

        while minHeap:
            currDistance, y, x = heapq.heappop(minHeap)

            if currDistance > dist[y][x]:
                continue

            nei = [(1,0), (-1,0), (0,1), (0,-1)]

            for i, j in nei:
                newY, newX = y + i, x + j

                if newX < 0 or newX >= COLS or newY < 0 or newY >= ROWS:
                    continue

                edgeDiff = abs(heights[newY][newX] - heights[y][x])
                newDist = max(currDistance, edgeDiff)

                if newDist < dist[newY][newX]:
                    dist[newY][newX] = newDist
                    heapq.heappush(minHeap, (newDist, newY, newX))

        return dist[ROWS-1][COLS-1]