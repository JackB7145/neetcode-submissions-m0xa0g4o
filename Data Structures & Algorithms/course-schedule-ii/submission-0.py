class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set()
        visited = set()

        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        res = []
        def dfs(curr):
            print(curr)
            if curr in path:
                return False
            if curr in visited:
                return True
            
            path.add(curr)
            for course in adj[curr]:
                if not dfs(course):
                    return False
                
            res.append(curr)
            path.remove(curr)
            visited.add(curr)
            return True
        
        print(adj)

        for course in adj:
            if not dfs(course):
                return []
        
        return res
                


            
            
            
            
            
