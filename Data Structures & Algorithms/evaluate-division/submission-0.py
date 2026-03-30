from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = {}  # weight[x] = x / parent[x]

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0

    def find(self, x):
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            root = self.find(orig_parent)

            # Path compression with weight adjustment
            self.weight[x] *= self.weight[orig_parent]
            self.parent[x] = root

        return self.parent[x]

    def union(self, x, y, value):
        self.add(x)
        self.add(y)

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # We want:
            # x / y = value
            #
            # x / rootX = weight[x]
            # y / rootY = weight[y]
            #
            # So:
            # rootX / rootY =
            # (value * weight[y]) / weight[x]

            ratio = (value * self.weight[y]) / self.weight[x]

            self.parent[rootX] = rootY
            self.weight[rootX] = ratio

    def isConnected(self, x, y):
        if x not in self.parent or y not in self.parent:
            return -1.0

        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            return -1.0

        # x/root * root/y
        return self.weight[x] / self.weight[y]


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        uf = UnionFind()

        # Build structure
        for (a, b), val in zip(equations, values):
            uf.union(a, b, val)

        # Answer queries
        result = []
        for a, b in queries:
            result.append(uf.isConnected(a, b))

        return result