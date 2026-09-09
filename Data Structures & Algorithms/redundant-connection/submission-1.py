class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]

        def union(u, v):
            a, b = find(u), find(v)

            if a != b:
                parents[b] = a
                return True

            return False

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])

            return parents[x]

        for a, b in edges:
            if not union(a, b):
                return [a, b]