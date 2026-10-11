from collections import deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # every letter that appears is a node, even with no edges
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for w1, w2 in zip(words, words[1:]):
            # invalid: a longer word appears before its own prefix
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:          # avoid counting a repeated edge twice
                        adj[a].add(b)
                        indegree[b] += 1
                    break                         # only the FIRST difference counts

        # start with letters that nothing has to come before
        q = deque(c for c in indegree if indegree[c] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # if a cycle exists, some letters never reach indegree 0
        return "".join(order) if len(order) == len(adj) else ""