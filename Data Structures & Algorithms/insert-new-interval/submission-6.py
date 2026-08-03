class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # stack = []
        # if not intervals:
        #     return [newInterval]

        # intervalUsed = False
        # for start, end in intervals:
        #     if stack and stack[-1][1] >= start:
        #         stack[-1][1] = max(stack[-1][1], end)
        #     elif start <= newInterval[0] <= end:
        #         stack.append([start, max(end, newInterval[1])])
        #         intervalUsed = True
        #     elif stack and stack[-1][1] < newInterval[0] and newInterval[1] < start:
        #         stack.append(newInterval)
        #         stack.append((start, end))
        #         intervalUsed = True
        #     else:
        #         stack.append((start, end))

        # if not 
        
        # return stack


        l, r = 0, len(intervals)-1
        while l <= r:
            m = (l+r)//2

            start, _ = intervals[m]

            if start <= newInterval[0]:
                l = m + 1
            
            else:
                r = m - 1

        intervals.insert(l, newInterval)

        stack = []
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])
        return stack

