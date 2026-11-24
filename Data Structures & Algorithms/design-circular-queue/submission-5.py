class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        # Build a ring of k nodes: head -> ... -> last -> head
        head = ListNode()
        cur = head
        for _ in range(k - 1):
            cur.nxt = ListNode()
            cur = cur.nxt
        cur.nxt = head
        self.front = head   # oldest element
        self.rear = cur     # newest element; the next write goes to rear.nxt

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = self.rear.nxt   # step forward around the ring
        self.rear.val = value       # overwrite the reused node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.nxt  # the old front's node becomes free to reuse
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap