class ListNode():
    def __init__(self, prev = None, next = None, val = None, key = None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.start = ListNode()
        self.end = None


    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]

            if len(self.mp) > 1:
                if not node.next:
                    self.end = node.prev.key
                
                #Moving the node to the beginning and moving the pointers around
                node.prev.next = node.next
                node.next = self.start.next

                if self.start.next:
                    self.start.next.prev = node

                self.start.next = node

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = ListNode(prev = self.start, next = self.start.next, val = value, key = key)

        if self.start.next:
            print(f'Moving ({newNode.key}, {newNode.val}) to front and setting ({self.start.next.key}, {self.start.next.val}) over one and setting prev')
            self.start.next.prev = newNode

        self.start.next = newNode
        self.mp[key] = newNode

        print('Received', key, value)
        
        #Check for capacity
        if len(self.mp) > self.capacity:
            
            print("Capacity Exceeded removing: ", self.end)
            #Remove the oldest used node
            endKey = self.end
            node = self.mp[endKey]
            self.end = node.prev.key
            del self.mp[endKey]
            node.prev.next = None

        if len(self.mp) == 1:
            self.end = key
        
