class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        heapq.heapify(minHeap)

        time = minHeap[0][0]
        res = []

        validHeap = []

        while minHeap or validHeap:
            while minHeap and minHeap[0][0] <= time:
                node = heapq.heappop(minHeap)
                heapq.heappush(validHeap, (node[1], node[2]))

            if not validHeap:
                time = minHeap[0][0]
                continue

            node = heapq.heappop(validHeap)

            res.append(node[1])
            time += node[0]

        return res