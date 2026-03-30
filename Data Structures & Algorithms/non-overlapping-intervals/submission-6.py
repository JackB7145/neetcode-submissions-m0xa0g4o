class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        When you have a conflict remove the bigger interval
         is going to be my strategy
        '''

        intervals.sort(key= lambda x: x[0])
        res = 0
        print(intervals)
        for i in range(len(intervals)):
            if i > 0 and intervals[i-1][1] > intervals[i][0]:
                print(f'Conflict between {intervals[i]} and {intervals[i-1]}')
                if (intervals[i][1] - intervals[i-1][0]) >= (intervals[i-1][1] - intervals[i-1][0]):
                    intervals[i] = intervals[i-1]

                res += 1
        
        return res

