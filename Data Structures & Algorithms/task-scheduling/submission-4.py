class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = []

        for num in freq:
            heapq.heappush(maxHeap, (-freq[num], num))

        queue = deque()

        time = 0

        '''
        maxheap = []
        queue = [(3, -2, 'A')]
        time = 3

        '''

        while maxHeap or queue:

            print(maxHeap, queue)

            while queue and queue[0][0] < time:
                node = queue.popleft()
                insertNode = (node[1], node[2])
                heapq.heappush(maxHeap, insertNode)

            if maxHeap:
                grabFirst = heapq.heappop(maxHeap)
                freq, task = grabFirst[0], grabFirst[1]

                if freq + 1 < 0:
                    queue.append((time+n, freq+1, task))

                time += 1

            else:
                time = queue[0][0] + 1

        return time

            

