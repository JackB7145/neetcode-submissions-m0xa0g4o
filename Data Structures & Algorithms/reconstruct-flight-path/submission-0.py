class Solution:
    def findItinerary(self, tickets):
        adj = defaultdict(list)
        edge_count = defaultdict(int)
        out_degree = defaultdict(int)

        for src, dst in tickets:
            adj[src].append(dst)
            edge_count[(src, dst)] += 1
            out_degree[src] += 1

        for node in adj:
            adj[node].sort()

        queue = deque(["JFK"])
        path = ["JFK"]

        while queue:
            current = queue.popleft()

            if current not in adj:
                continue

            next_airport = None

            for dest in adj[current]:
                if edge_count[(current, dest)] > 0:
                    next_airport = dest
                    break

            if next_airport:
                edge_count[(current, next_airport)] -= 1
                out_degree[current] -= 1

                queue.append(next_airport)
                path.append(next_airport)

        return path