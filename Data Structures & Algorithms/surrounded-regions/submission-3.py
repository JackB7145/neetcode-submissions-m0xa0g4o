class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])

        seen = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            board[i][j] = "D"
            seen[i][j] = True

            for di, dj in dirs:
                nI, nJ = i + di, j + dj

                if (
                    0 <= nI < rows
                    and 0 <= nJ < cols
                    and board[nI][nJ] == "O"
                    and not seen[nI][nJ]
                ):
                    dfs(nI, nJ)

        # Find all O's connected to the border
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)

            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)

            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        # Capture surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"
