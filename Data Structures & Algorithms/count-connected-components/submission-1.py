class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def union(u, v):
            a, b = find(u), find(v)

            if a != b:
                parents[a] = b

        def find(x):
            while x != parents[x]:
                x = parents[x]
            
            return x

        for a, b in edges:
            union(a, b)
        
        return len({find(i) for i in parents})
