class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        path = set()
        visited = set()
        
        def dfs(curr, prev):
            if curr in path:
                return False
            
            path.add(curr)

            for nei in adj[curr]:
                if nei != prev and not dfs(nei, curr):
                    return False

            path.remove(curr)
            visited.add(curr)

            return True

        res = dfs(0, -1)
        for i in range(1, n):
            if i not in visited:
                return False
        
        return res