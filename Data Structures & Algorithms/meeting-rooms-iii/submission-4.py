import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = [0 for _ in range(n)]
        c = []
        o = [i for i in range(n)]
        heapq.heapify(meetings)
        while meetings:
            meeting_start, meeting_end = heapq.heappop(meetings)
            while c and c[0][0] <= meeting_start:
                _, room_id = heapq.heappop(c)
                heapq.heappush(o, room_id)
            if not o:
                room_opens, room_id = heapq.heappop(c)
                room_closes = room_opens + meeting_end - meeting_start
            else:
                room_id = heapq.heappop(o)
                room_closes = meeting_end
            heapq.heappush(c, (room_closes, room_id))
            ans[room_id] += 1
        
        res = 0
        for i in range(len(ans)):
            if ans[i] > ans[res]:
                res = i
        return res