from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Nodes with only one neighbor are leaves
        leaves = deque()

        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)

        remaining = n

        while remaining > 2:
            # Remove the current layer of leaves
            leaf_count = len(leaves)
            remaining -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)

                    # Neighbor became a leaf
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)

        return list(leaves)