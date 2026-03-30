"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if not intervals:
            return True
        last = intervals[0]
        for interval in intervals[1:]:
            if not(last.end <= interval.start):
                return False
            last = interval
        return True