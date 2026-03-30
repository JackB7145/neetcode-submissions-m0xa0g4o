class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0
        adj = [[] for _ in range(n)]

        for src, dst, weight in times:
            adj[src-1].append((dst-1, weight))

        heap = [(0, k-1)]

        visited = set()
        while heap:
            currDist, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)

            for nei, cost in adj[node]:
                newDist = cost + currDist
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(heap, (newDist, nei))
            

        return max(dist) if max(dist) < float('inf') else -1
