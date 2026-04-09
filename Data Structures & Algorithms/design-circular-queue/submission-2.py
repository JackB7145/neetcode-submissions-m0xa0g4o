class listNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class MyCircularQueue:

    def __init__(self, k: int):
        self.total = k
        self.nodesLeft = k
        self.end = listNode()
        self.start = listNode(next=self.end)
        self.end.prev = self.start
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = listNode(value, self.start.next)
        self.start.next.prev = newNode
        self.start.next = newNode
        self.nodesLeft -= 1
        print(self.start.next)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.end.prev = self.end.prev.prev
        self.end.prev.next = self.end
        self.nodesLeft += 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.prev.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.start.next.val

    def isEmpty(self) -> bool:
        return self.nodesLeft == self.total

    def isFull(self) -> bool:
        return self.nodesLeft == 0



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()