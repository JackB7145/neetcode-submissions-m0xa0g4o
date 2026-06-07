import heapq
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.heap = []
        self.mp = defaultdict(int)
        self.counter = 0  # global insertion order

    def push(self, val: int) -> None:
        self.mp[val] += 1
        self.counter += 1

        # (-freq, -counter, val) → max heap behavior
        heapq.heappush(self.heap, (-self.mp[val], -self.counter, val))

    def pop(self) -> int:
        while self.heap:
            freq, _, val = heapq.heappop(self.heap)
            freq = -freq

            # lazy deletion check
            if val in self.mp and self.mp[val] == freq:
                self.mp[val] -= 1
                if self.mp[val] == 0:
                    del self.mp[val]
                return val