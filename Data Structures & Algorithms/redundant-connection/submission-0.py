class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        stack = []
        in_stack = set()
        cycle = set()
        found = False

        def dfs(node, parent):
            nonlocal found
            if found:
                return

            visited.add(node)
            stack.append(node)
            in_stack.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if nei in in_stack:
                    # extract cycle safely
                    idx = stack.index(nei)
                    cycle.update(stack[idx:])
                    found = True
                    return

                if nei not in visited:
                    dfs(nei, node)
                    if found:
                        return

            # only clean up if NO cycle was found
            stack.pop()
            in_stack.remove(node)

        dfs(edges[0][0], -1)

        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
