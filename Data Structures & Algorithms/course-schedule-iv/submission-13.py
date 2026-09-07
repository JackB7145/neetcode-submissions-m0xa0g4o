class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(curr, target, visited):
            if curr == target:
                return True

            if curr in visited:
                return False

            visited.add(curr)

            for nei in adj[curr]:
                if dfs(nei, target, visited):
                    return True

            return False

        res = []

        for u, v in queries:
            res.append(dfs(u, v, set()))

        return res