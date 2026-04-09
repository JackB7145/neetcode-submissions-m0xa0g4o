class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def checkSurrounding(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] == 'X':
                return
            
            board[i][j] = 'Z'
            checkSurrounding(i+1, j)
            checkSurrounding(i-1, j)
            checkSurrounding(i, j+1)
            checkSurrounding(i, j-1)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            checkSurrounding(r, 0)
            checkSurrounding(r, COLS-1)
        
        for c in range(COLS):
            checkSurrounding(0, c)
            checkSurrounding(ROWS-1, c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'

            