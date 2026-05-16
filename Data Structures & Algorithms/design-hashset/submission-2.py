class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr.append(key)
        

    def remove(self, key: int) -> None:
        idx = self.arr.index(key) if key in self.arr else -1
        if idx < 0:
            return
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()

    def contains(self, key: int) -> bool:
        return key in self.arr


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)