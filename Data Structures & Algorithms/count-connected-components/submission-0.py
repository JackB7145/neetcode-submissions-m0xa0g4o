class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def traverse(curr):
            if curr in visited:
                return
            
            visited.add(curr)
            for edg in adj[curr]:                
                traverse(edg)
    
        res = 0
        for start in range(n):
            size = len(visited)
            traverse(start)
            if len(visited) > size:
                res += 1
        
        return res
