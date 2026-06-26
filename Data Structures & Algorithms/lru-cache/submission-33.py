class ListNode:
    def __init__(self, val=0, key=-1):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}

        # dummy nodes
        self.start = ListNode()
        self.end = ListNode()

        self.start.next = self.end
        self.end.prev = self.start

    # 🔹 remove a node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 🔹 insert node right after start (most recent)
    def insert_front(self, node):
        node.next = self.start.next
        node.prev = self.start
        self.start.next.prev = node
        self.start.next = node

    # 🔹 mark node as recently used
    def use(self, key):
        node = self.mp[key]
        self.remove(node)
        self.insert_front(node)

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        self.use(key)
        return self.mp[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.use(key)
            return

        node = ListNode(value, key)
        self.mp[key] = node
        self.insert_front(node)

        if len(self.mp) > self.capacity:
            # remove LRU (node before end)
            lru = self.end.prev
            self.remove(lru)
            del self.mp[lru.key]