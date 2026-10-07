class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0

        minHeap = [(0, 0, 0)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            cost, i, j = heapq.heappop(minHeap)

            if (i, j) == (rows - 1, cols - 1):
                return cost

            # Ignore an outdated heap entry
            if cost > dist[i][j]:
                continue

            for di, dj in dirs:
                newI = i + di
                newJ = j + dj

                if not (0 <= newI < rows and 0 <= newJ < cols):
                    continue

                diff = abs(heights[i][j] - heights[newI][newJ])
                newCost = max(cost, diff)

                if newCost < dist[newI][newJ]:
                    dist[newI][newJ] = newCost
                    heapq.heappush(minHeap, (newCost, newI, newJ))

        return -1
