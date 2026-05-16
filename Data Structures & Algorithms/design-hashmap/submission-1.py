class MyHashMap:

    def __init__(self):
        self.keys = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.keys[key] = value
        
    def get(self, key: int) -> int:
        return self.keys[key]

    def remove(self, key: int) -> None:
        self.keys[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)