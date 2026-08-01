class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        cols = set()
        posDag = set()
        negDag = set()

        def backtrack(row):
            nonlocal res
            if row >= n:
                res += 1
                return
            
            for col in range(n):
                if col not in cols and col + row not in posDag and col - row not in negDag:
                    cols.add(col)
                    posDag.add(col + row)
                    negDag.add(col - row)
                    backtrack(row+1)
                    cols.remove(col)
                    posDag.remove(col + row)
                    negDag.remove(col - row)


        backtrack(0)
        return res
