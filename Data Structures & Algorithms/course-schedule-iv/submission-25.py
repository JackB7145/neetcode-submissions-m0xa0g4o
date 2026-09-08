class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        cache = {}
        visited = set()

        def dfs(curr, target):
            if curr == target:
                return True

            if (curr, target) in cache:
                return cache[(curr, target)]

            for nei in adj[curr]:
                if dfs(nei, target):
                    cache[(curr, target)] = True
                    return True

            cache[(curr, target)] = False
            return False

        res = []

        for u, v in queries:
            res.append(dfs(u, v))

        return res