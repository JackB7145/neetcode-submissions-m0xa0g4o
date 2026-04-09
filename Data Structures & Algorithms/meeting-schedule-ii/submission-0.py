"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = []
        intervals.sort(key=lambda x:x.start)
        for i, interval in enumerate(intervals):
            start, end = interval.start, interval.end
            found = False
            for i in range(len(res)):
                if res[i][-1][1] >= start:
                    continue
                else:
                    res[i].append((start, end))

            if not found:
                res.append([(start, end)])
        print(res)
        return len(res)
                    