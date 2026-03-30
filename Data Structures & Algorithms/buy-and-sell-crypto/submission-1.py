class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i in prices:   
            low = min(i, low)
            profit = max(i-low, profit)
        return profit