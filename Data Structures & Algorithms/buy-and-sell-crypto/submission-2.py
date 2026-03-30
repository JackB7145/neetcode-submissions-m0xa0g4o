class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        res = 0
        for price in prices:
            smallest = min(smallest, price)
            res = max(res, price - smallest)
        return res