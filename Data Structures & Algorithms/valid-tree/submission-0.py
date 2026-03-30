class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        I think I just need to check for a root, if I can find a root that everything navigates
        to it's true. A Tree is a type of graph, that is directed (But in this instance we are given undirected so I imagine it's fine)

        So we just do a recursive function that travers

        Criteria of a tree

        A connected, noncyclical graph? I guess that is the criteria I'm looking for 
        '''
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        path = set()
        visited = set()

        def traverse(curr, prev):
            if curr in path:
                return False
            if curr in visited:
                return True
            
            path.add(curr)

            for edg in adj[curr]:
                if edg == prev:
                    continue
                
                if not traverse(edg, curr):
                    return False
                
            visited.add(curr)
            path.remove(curr)
            return True
        
        if not traverse(0, -1):
            return False
        
        if len(visited) != n:
            return False
    
        return True
            
