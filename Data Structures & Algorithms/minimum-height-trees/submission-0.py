from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        graph = defaultdict(list)
        degree = [0] * n
        
        # Build graph and track degrees
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Start with all leaves
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        
        remaining_nodes = n
        
        # Trim leaves layer by layer
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
