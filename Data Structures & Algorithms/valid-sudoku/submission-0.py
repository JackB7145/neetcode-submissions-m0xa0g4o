class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validateRow():
            valid = True
            for i in range(len(board)):
                print(board[i])
                if not(validateNumbers(board[i])):
                    valid = False
            return valid
                
        def validateColumn():
            valid = True
            for j in range(len(board)):
                new = []
                for i in range(len(board)):
                    new.append(board[i][j])
                if not(validateNumbers(new)):
                    valid = False
            return valid
        
        def validateBox():
            valid = True
            for i in range(1, len(board), 3):
                for j in range(1, len(board), 3):
                    new = [board[i-1][j-1], board[i][j-1], board[i+1][j-1], board[i-1][j], board[i][j], board[i+1][j], board[i-1][j+1], board[i][j+1], board[i+1][j+1]]
                    if not(validateNumbers(new)):
                        valid = False
            return valid

        def validateNumbers(sequence):
            valid = True
            for i in range(1, len(sequence)-1):
                new = sequence[0:i-1] + sequence[i+1:len(sequence)]
                if new.count(sequence[i]) != 0:
                    valid = False
            
            return valid

        print("Valid Rows: ", validateRow())
        print("Valid Columns: ", validateColumn())
        print("Valid Boxes: ", validateBox())
        return validateRow() and validateColumn() and validateBox()

                