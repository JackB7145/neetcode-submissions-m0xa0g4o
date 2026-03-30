class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''

        First solution:

        Horizontally scan n intervals for m queries with a time complexity of O(n*m)

        Second solution:

        First you could go through every interval, recording the numbers in the interval
        and the size of the overal interval, only keeping the smallest one. 

        Then you could do a second pass with the queries taking the smallest recorded
        one in the map 

        The first operation would be O(n*k + m) where n is the length of queries, k is the range of numbers
        and m is the number of queires

        Third solution:

        
        '''

        # res = []
        # intervals.sort(key= lambda x: x[0])
        # print("Intervals: ", intervals)
        # print("Queries: ", queries)
        # for query in queries:
        #     smallest = float('inf')
        #     for start, end in intervals:
        #         if not (start <= query <= end):
        #             continue
                
        #         smallest = min(smallest, end-start+1)
            
        #     if smallest < float('inf'):
        #         res.append(smallest)
        #     else:
        #         res.append(-1)
                    
        # return res

        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
