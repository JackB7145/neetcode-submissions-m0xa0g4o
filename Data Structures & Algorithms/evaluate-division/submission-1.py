class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = {}

        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, value in graph[curr]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1:
                    return value * result

            return -1

        answer = []

        for a, b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a, b, set()))

        return answer