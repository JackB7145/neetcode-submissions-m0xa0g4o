class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        count = 1
        while count ** 2 <= n:
            squares.append(count**2)
            count += 1

        res = 0
        for i in range(len(squares)-1, -1, -1):
            square = squares[i]
            cnt = n // square
            n -= cnt * square
            res += cnt
        
        return res