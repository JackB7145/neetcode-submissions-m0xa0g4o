class Solution:
    def solveNQueens(self, n: int):

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        cols = set()
        dag = set()  # stores queen positions

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                isValid = col not in cols

                # temp store of what we'll remove
                removable = []

                for i, j in dag:
                    diff = row - i
                    left = (i + diff, j - diff)
                    right = (i + diff, j + diff)

                    # if both projected diagonals are off-board → prune later
                    if left[1] < 0 and right[1] >= n:
                        removable.append((i, j))

                    # standard conflict check
                    if (row, col) == left or (row, col) == right:
                        isValid = False

                if not isValid:
                    continue

                # apply cleanup for this branch only
                for r in removable:
                    dag.remove(r)

                cols.add(col)
                dag.add((row, col))
                board[row][col] = "Q"

                backtrack(row + 1)

                # undo
                board[row][col] = "."
                dag.remove((row, col))
                cols.remove(col)

                # restore removed diagonals (critical)
                for r in removable:
                    dag.add(r)

        backtrack(0)
        return res
