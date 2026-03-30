class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(r, c):
            # Check column
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            # Check top-left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check top-right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if isValid(r, c):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'

        backtrack(0)
        return res
