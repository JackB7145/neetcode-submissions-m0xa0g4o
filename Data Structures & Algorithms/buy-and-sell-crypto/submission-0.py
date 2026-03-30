class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        profit = 0
        for i in range(len(prices)):
            small = min(small, prices[i])
            profit = max(profit, prices[i] - small)
            
        return profit
