class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        visited = {}
        adj = [[] for _ in range(n)]

        minHeap = [(0, 0, src)] 
        dist[k-1] = 0
        
        for src, dst, cost in flights:
            adj[src].append((cost, dst))
        
        while minHeap:
            currDist, flight, node = heapq.heappop(minHeap)

            if node in visited and visited[node] < flight or flight > k:
                continue
            
            visited[node] = flight

            for cost, nei in adj[node]:
                newDist = currDist + cost
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(minHeap, (newDist, flight + 1, nei))
            
        return dist[dst]
