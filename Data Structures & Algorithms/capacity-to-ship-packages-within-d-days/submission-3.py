class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def calculateDays(limit):
            dCnt = 0
            total = 0
            for weight in weights:
                if total + weight > limit:
                    total = 0
                    dCnt += 1 
                total += weight

            res = dCnt + math.ceil(total/limit)

            return res

        l, r = max(weights), sum(weights)

        while l <= r:
            c = (l+r)//2

            d = calculateDays(c)

            if d <= days:
                r = c - 1
                val = c
            
            else:
                l = c + 1

        
        return val