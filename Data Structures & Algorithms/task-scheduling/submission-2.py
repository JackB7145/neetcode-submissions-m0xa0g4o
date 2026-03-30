class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Manually count frequencies of tasks
        freq_map = {}
        for task in tasks:
            if task in freq_map:
                freq_map[task] += 1
            else:
                freq_map[task] = 1

        # Create max heap from negative counts
        maxHeap = [-cnt for cnt in freq_map.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, readyTime]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                # Jump time forward to when the next task is ready
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time