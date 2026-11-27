class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        why dont we just use a prefix suffix array

        keeping track of the maximum and the minimum and then finding the difference and then reutnring the maximum
        '''
        profit = 0

        pre = []
        smallest = 10e9
        for p in prices:
            smallest = min(smallest, p)
            pre.append(smallest)

        largest = -10e9
        for i in range(len(prices)-1, -1, -1):
            largest = max(largest, prices[i])
            profit = max(largest-pre[i], profit)

        return profit