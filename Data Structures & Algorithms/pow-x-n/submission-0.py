class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1/x
        for _ in range(abs(n)):
            res *= x
        
        return res