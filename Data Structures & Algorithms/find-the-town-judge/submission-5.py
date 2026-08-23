class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # seen = defaultdict(int)
        # visited = set()

        # adj = [[] for _ in range(n)]

        # for a, b in trust:
        #     adj[a-1].append(b-1)

        # def dfs(curr):
        #     if curr in visited:
        #         return
            
        #     visited.add(curr)
        #     for node in adj[curr]:
        #         dfs(node)
            
        #     visited.remove(curr)
        #     print(curr)
        #     seen[curr] += 1

        # print(adj)
        # for i in range(n):
        #     dfs(i)

        # print(seen)

        # if max(seen.values()) != n:
        #     return -1
            
        # for node in seen:
        #     if seen[node] == n:
        #         return node+1
        adj = [[] for _ in range(n)]
        cnt = defaultdict(int)
        for a, b in trust:
            adj[a-1].append(b-1)
            cnt[b-1] += 1

        
        print(cnt)
        print(adj)

        if max(cnt.values()) != n-1:
            return -1

        for node in cnt:
            if cnt[node] == n-1 and not len(adj[node]):
                return node+1
        return -1

        


