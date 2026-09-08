class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def union(u, v):
            a, b = find(u), find(v)

            if a != b:
                parents[a] = b

        def find(x):
            end = x
            if x != parents[x]:
                end = find(parents[x])
                parents[x] = end
            return end

        for a, b in edges:
            union(a, b)
        
        return len({find(i) for i in parents})
