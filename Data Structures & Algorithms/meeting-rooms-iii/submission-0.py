import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []  # (end_time, room)

        roomsCnt = [0] * n

        for start, end in meetings:

            # free finished rooms
            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                finish, room = heapq.heappop(busy)
                duration = end - start
                end = finish + duration
                heapq.heappush(busy, (end, room))

            roomsCnt[room] += 1

        res = 0
        for i in range(1, n):
            if roomsCnt[i] > roomsCnt[res]:
                res = i

        return res