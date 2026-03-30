class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def getSum(num: int) -> int:
            res = 0
            while num:
                digit = num % 10
                num //= 10
                res += digit ** 2
            
            return res
                
        while n not in [0, 1]:
            if n in seen:
                return False
            seen.add(n)
            n = getSum(n)
        return True