class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def loadShip(limit: int)->int:
            res = 0
            total = 0
            for weight in weights:
                if weight + total > limit:
                    res += 1
                    total = weight
                else:
                    total += weight

            return 1 + res


        l, r = max(weights), sum(weights)
        res = 10e9

        while l <= r:
            m = (l+r)//2
            d = loadShip(m)

            if d <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res

