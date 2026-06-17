class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = float('inf')
        for i in range(len(prices)):
            profit = max(prices[i]-low, profit)
            low = min(low, prices[i])

        
        return profit