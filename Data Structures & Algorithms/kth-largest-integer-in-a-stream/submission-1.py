class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-x for x in nums]
        heapq.heapify(self.heap)
        self.k = k
    def add(self, val: int) -> int:
        value = self.heap.pop(self.k//2)
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, -val)
        return -value
