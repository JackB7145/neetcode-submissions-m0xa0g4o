"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        startTimes = []  # 1, 2, 4, 7
        endTimes = []    # 2, 3, 8, 10
        
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()
        
        endIdx = 0
        
        res = 0
        currentMeetings = 0
        
        for start in startTimes:  # Iterate through each start time
            while start >= endTimes[endIdx]:  # When we find that our start time is after our earliest end time, we can say the meeting has ended
                currentMeetings -= 1
                endIdx += 1
                
            currentMeetings += 1
            res = max(res, currentMeetings)  # 1
        
        return res