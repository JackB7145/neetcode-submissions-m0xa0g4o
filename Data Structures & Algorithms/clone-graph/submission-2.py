"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def __init__(self):
        self.seen = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node in self.seen:
            return self.seen[node]

        newNode = Node(node.val)
        self.seen[node] = newNode  

        for nei in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(nei))

        return newNode