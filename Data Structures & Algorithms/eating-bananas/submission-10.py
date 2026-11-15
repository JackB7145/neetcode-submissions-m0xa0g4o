class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHours(rate):
            res = 0
            for n in piles:
                res += math.ceil(n/rate)
            
            return res

    
        l, r = 1, max(piles)
        res = 10e9
        while l <= r:
            rate = (l+r)//2

            hours = findHours(rate)

            if hours <= h:
                res = min(rate, res)
                r = rate - 1
            else:
                l = rate + 1

            
        
        return res