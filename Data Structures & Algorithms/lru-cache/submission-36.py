class Node:
    def __init__(self, val=0, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        self.start = Node()   # dummy head: start.next is the least recently used
        self.end = Node()     # dummy tail: end.prev is the most recently used
        self.coupleNodes(self.start, self.end)

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.useNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
        else:
            self.mp[key] = Node(value, key)

        self.useNode(self.mp[key])

        if len(self.mp) > self.capacity:
            lruNode = self.start.next
            self.uncoupleNode(lruNode)
            del self.mp[lruNode.key]

    def coupleNodes(self, a, b):
        a.next = b
        b.prev = a

    def uncoupleNode(self, a):
        if a.prev and a.next:
            self.coupleNodes(a.prev, a.next)
        a.prev = a.next = None

    def useNode(self, a):
        # Move a to the most-recently-used position, just before end
        self.uncoupleNode(a)
        self.coupleNodes(self.end.prev, a)
        self.coupleNodes(a, self.end)