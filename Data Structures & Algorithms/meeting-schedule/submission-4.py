"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        for i,v in enumerate(intervals):
            start = v.start
            end = v.end
            if i > 0 and start <= intervals[i-1].end:
                return False
        return True