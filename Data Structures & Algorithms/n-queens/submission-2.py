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
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        cols = set()
        dag = set()
        def backtrack(row):
            if row >= len(board):
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                isValid = not(col in cols)
                remove = []

                for i, j in dag:
                    diff = row - i
                    left = (i+diff, j-diff)
                    right = (i+diff, j+diff)
                    if left[1] < 0 and right[1] < 0:
                        remove.append((i, j))

                    if (row, col) in [left, right]:
                        isValid = False
                
                for removeDag in remove:
                    dag.remove(removeDag)
                
                if not isValid:
                    continue
                
                cols.add(col)
                dag.add((row, col))
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'
                cols.remove(col)
                dag.remove((row, col))

                for removeDag in remove:
                    dag.add(removeDag)
        backtrack(0)
        return res
            