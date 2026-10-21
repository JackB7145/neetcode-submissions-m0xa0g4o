class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validSquare(x, y):
            seen = set()
            a = x + 3
            b = y + 3
            for i in range(x, a):
                for j in range(y, b):
                    c = board[i][j]
                    if c in seen and c != ".":
                        return False
                    seen.add(c)
            
            return True

        def validRow(ROW):
            seen = set()
            for j in range(9):
                c = board[ROW][j] 
                if c in seen and c != ".":
                    return False
                seen.add(c)
            return True
        
        def validCol(COL):
            seen = set()
            for i in range(9):
                c = board[i][COL]
                if c in seen and c != ".":
                    return False
                seen.add(c)
            return True

        for row in board:
            print(row)

        for i in range(9):
            if not validRow(i) or not validCol(i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not validSquare(i, j):
                    return False
        
        return True
        
            


