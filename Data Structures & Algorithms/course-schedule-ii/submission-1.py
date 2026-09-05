class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b)

        path = set()
        visited = set()

        def dfs(curr):
            nonlocal res

            if curr in path:
                return False
            
            path.add(curr)
            
            for nei in adj[curr]:
                if nei not in visited:
                    if not dfs(nei):
                        return False

            path.remove(curr)
            res.append(curr)
            visited.add(curr)
            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return []
        
        return res