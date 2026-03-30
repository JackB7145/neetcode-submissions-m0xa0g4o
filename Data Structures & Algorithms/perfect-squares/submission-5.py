class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        memo = {}

        def findMinimum(total):
            if total == n:
                return 0
            if total > n:
                return float('inf')
            if total in memo:
                return memo[total]

            res = float('inf')
            for sq in squares:
                # if total + sq > n:
                #     break
                res = min(res, 1 + findMinimum(total + sq))

            memo[total] = res
            return res

        return findMinimum(0)