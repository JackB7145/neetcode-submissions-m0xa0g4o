class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b)

        path = set()
        visited = set()

        def dfs(curr):
            if curr in path:
                return False
            
            path.add(curr)
            for nei in adj[curr]:
                if nei not in visited and not dfs(nei):
                    return False
            
            path.remove(curr)
            visited.add(curr)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True