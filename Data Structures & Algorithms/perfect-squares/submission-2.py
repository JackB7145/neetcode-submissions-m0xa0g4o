from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        count = 1
        while count ** 2 <= n:
            squares.append(count**2)
            count += 1

        @lru_cache
        def findMinimum(total, cnt):
            if total == n:  
                return cnt
            elif total >= n:
                return float('inf')
            
            res = float('inf')
            for i in range(len(squares)):
                res = min(res, findMinimum(total+squares[i], cnt+1))
            
            return res
        
        return findMinimum(0, 0)
