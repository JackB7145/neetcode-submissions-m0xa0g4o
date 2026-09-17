class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def findChange(left):
            if left in cache:
                return cache[left]
            elif left == 0:
                return 0
            elif left < 0:
                return 10**28
            
            res = 10**28
            for c in coins:
                ans = findChange(left-c)
                if ans < 0:
                    continue

                res = min(res, 1+ans)
                
            if res >= 10**28:
                cache[left] = -1
                return -1

            cache[left] = res
            return res
        
        return findChange(amount)
