class ListNode:
    def __init__(self, prev=None, next=None, val=None, key=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}

        # Dummy head and dummy tail
        self.start = ListNode()     # head
        self.end = ListNode()       # tail

        self.start.next = self.end
        self.end.prev = self.start

    # Remove a node from the linked list
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert a node right after head (most recent)
    def _insert_front(self, node):
        node.next = self.start.next
        node.prev = self.start
        self.start.next.prev = node
        self.start.next = node

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        node = self.mp[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
            return

        # create new node
        newNode = ListNode(val=value, key=key)
        self.mp[key] = newNode
        self._insert_front(newNode)

        # eviction if over capacity
        if len(self.mp) > self.capacity:
            # LRU = node before tail
            lru = self.end.prev
            self._remove(lru)
            del self.mp[lru.key]
