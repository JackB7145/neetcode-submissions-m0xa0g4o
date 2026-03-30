class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = float('inf')
        for n in prices:
            if n > prev:
                profit += n - prev
            prev = n

        return profit