class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        while self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            num1 = -heapq.heappop(self.maxHeap)
            num2 = heapq.heappop(self.minHeap)

            heapq.heappush(self.maxHeap, -num2)
            heapq.heappush(self.minHeap, num1)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            num1 = -self.maxHeap[0]
            num2 = self.minHeap[0]

            res = (num1 + num2)/2
        else:
            res = -self.maxHeap[0]
        
        print(self.maxHeap, self.minHeap, res)
        return res
        
        