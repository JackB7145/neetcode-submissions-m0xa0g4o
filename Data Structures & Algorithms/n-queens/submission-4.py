class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]

        rows = set()
        cols = set()
        posDag = set()
        negDag = set()
        
        def backtrack(row):
            if row >= n:
                res.append(getBoardFormat())
                return
            
            for col in range(n):
                if handleRow(row) and handleCol(col) and handleDia(row, col):
                    addAll(row, col)
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
                    removeAll(row, col)

        def handleRow(row):
            return row not in rows

        def handleCol(col):
            return col not in cols

        def handleDia(row, col):
            pos = col + row
            neg = col - row
            return pos not in posDag and neg not in negDag

        def getBoardFormat():
            return ["".join(row) for row in board]  # ✅ FIXED

        def addAll(row, col):
            rows.add(row)
            cols.add(col)
            posDag.add(col + row)
            negDag.add(col - row)

        def removeAll(row, col):
            rows.remove(row)
            cols.remove(col)
            posDag.remove(col + row)
            negDag.remove(col - row)

        backtrack(0)
        return res