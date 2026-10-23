class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        hold = prices[0]
        for n in prices[1:]:
            if n > hold:
                res += n - hold
                hold = n
            hold = min(hold, n)
        return res