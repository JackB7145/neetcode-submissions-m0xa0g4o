class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rows in board:
            print(rows)

        for i in range(len(board)):
            used = set()
            for j in range(len(board[0])):
                if board[i][j] in used and board[i][j] != '.':
                    return False
                used.add(board[i][j])

        
        for j in range(len(board[0])):
            used = set()
            for i in range(len(board)):
                if board[i][j] in used and board[i][j] != '.':
                    return False
                used.add(board[i][j])


        startingPoints = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for x, y in startingPoints:
            used = set()
            for i in range(y, y+3):
                for j in range(x, x+3):
                    if board[i][j] in used and board[i][j] != '.':
                        return False
                    used.add(board[i][j])

        
        return True