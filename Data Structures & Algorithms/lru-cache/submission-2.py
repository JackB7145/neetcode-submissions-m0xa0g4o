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
                if node.next == None:
                    self.end = node.prev.key
                
                #Moving the node to the beginning and moving the pointers around
                node.prev.next = node.next
                node.next = self.start.next
                self.start.next = node

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = ListNode(prev = self.start, next = self.start.next, val = value, key = key)
        self.start.next = newNode
        self.mp[key] = newNode

        print(key, value)
        
        #Check for capacity
        if len(self.mp) > self.capacity:
            
            print("Capacity Exceeded removing: ", self.end)
            #Remove the oldest used node
            endKey = self.end
            node = self.mp[endKey]
            del self.mp[endKey]
            node.prev.next = None

        if len(self.mp) == 1:
            self.end = key
        
