class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        

        return res
        '''
        The strategy of this question is to minimize the chances of another conflict. So we check for conflicts like your normal merge intervals, if 
        if there is an issue, we have to remove one, we need to be stragegic about removing the one with that is least likely ot create anohter issue

        How we do this, is we remove the one which has an end closest to the start, meaning the smallest possible end beween the two. Since that's what will
        control the liklihood of a confict -> The size of the interval and where it is (That's why we want the smallest of the previous end and current end)
        '''