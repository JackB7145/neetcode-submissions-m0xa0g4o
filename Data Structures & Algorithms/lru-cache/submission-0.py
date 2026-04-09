class ListNode():
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        print("New Node")


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = ListNode()

    def display(self, list1):
        curr = list1
        while curr:
            print(curr.val, end=" -> ")
            if not curr.val:
                print(curr.val)
                break
            curr = curr.next
        
    def get(self, key: int) -> int:
        curr = self.cache.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity:
            curr = self.cache
            while curr.next:
                curr = curr.next
            curr.next = ListNode(key, value, None)

        else:
            self.cache.next = self.cache.next.next
            curr = self.cache.next
            while curr.next:
                curr = curr.next
            curr.next = ListNode(key, value, None)

        self.capacity -= 1
        self.display(self.cache)
        
