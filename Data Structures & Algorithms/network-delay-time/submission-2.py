class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, t in times:
            adj[u-1].append((v-1, t))

        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0

        minHeap = [(0, k-1)]

        while minHeap:
            currTime, node = heapq.heappop(minHeap)

            for nxt, timeCost in adj[node]:
                newTime = currTime + timeCost
                if newTime < dist[nxt]:
                    dist[nxt] = newTime
                    heapq.heappush(minHeap, (newTime, nxt))



        if float('inf') in dist:
            return -1

        return max(dist)