class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        path = set()
        visited = set()

        def dfs(curr):
            if curr in path:
                return False
            if curr in visited:
                return True

            path.add(curr)
            for nxt in adj[curr]:
                if not dfs(nxt):
                    return False
            path.remove(curr)
            visited.add(curr)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
