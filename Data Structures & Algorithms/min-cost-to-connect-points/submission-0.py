class Solution:


    def minCostConnectPoints(self, points):
        n = len(points)

        dist = [float('inf')] * n
        visited = [False] * n

        dist[0] = 0
        heap = [(0, 0)]  # (cost, node)

        total_cost = 0

        while heap:
            cost, node = heapq.heappop(heap)

            if visited[node]:
                continue

            visited[node] = True
            total_cost += cost

            x1, y1 = points[node]

            for next_node in range(n):
                if not visited[next_node]:
                    x2, y2 = points[next_node]

                    manhattan = abs(x1 - x2) + abs(y1 - y2)

                    if manhattan < dist[next_node]:
                        dist[next_node] = manhattan
                        heapq.heappush(heap, (manhattan, next_node))

        return total_cost        