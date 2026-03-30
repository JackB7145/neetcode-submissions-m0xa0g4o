class Solution:
    def solveNQueens(self, n: int):
        '''
        We focus on row by row, keeping track of the valid colums as we go, and keeping track of the valid diagonals

        How do we do the diagonals. We could calculate a conflict by projecting wheere the diagonal would land at our row. if that spot is in our current spot
        it is not valid

        e.g. Say we are going row by row on a board of size n. We place a queen on (1, 1)
        When we are at row 3. we know that the left diagonal is not a problem, but the right diagonal is a concern. We find the distance between
        the current row and the row of the queen, and go right or left from the x position that amount. While the diagonals on both sides are out of range we 
        remove from our set of diagonals

        '''
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
            