from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    """Doubly linked list: head side = least recent, tail side = most recent."""
    def __init__(self):
        self.head = Node(0, 0)   # sentinel
        self.tail = Node(0, 0)   # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):          # add as most recent
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node):          # O(1) removal from anywhere
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_lru(self):               # remove least recent
        node = self.head.next
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}                    # key -> Node
        self.freqs = defaultdict(DLL)      # freq -> DLL (LRU order)
        self.min_freq = 0

    def _touch(self, node):
        """Move node from its freq bucket to freq+1."""
        f = node.freq
        self.freqs[f].remove(node)
        if self.freqs[f].size == 0:
            del self.freqs[f]
            if self.min_freq == f:
                self.min_freq += 1
        node.freq += 1
        self.freqs[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._touch(node)
            return
        if len(self.nodes) == self.cap:
            lru = self.freqs[self.min_freq].pop_lru()
            if self.freqs[self.min_freq].size == 0:
                del self.freqs[self.min_freq]
            del self.nodes[lru.key]
        node = Node(key, value)
        self.nodes[key] = node
        self.freqs[1].append(node)
        self.min_freq = 1