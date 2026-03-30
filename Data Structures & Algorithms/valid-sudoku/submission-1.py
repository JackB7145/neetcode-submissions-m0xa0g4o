class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validateRow():
            valid = True
            for i in range(len(board)):
                if not(validateNumbers(board[i], "Row")):
                    valid = False
            return valid
                
        def validateColumn():
            valid = True
            for j in range(len(board)):
                new = []
                for i in range(len(board)):
                    new.append(board[i][j])
                if not(validateNumbers(new, "Column")):
                    valid = False
            return valid
        
        def validateBox():
            valid = True
            for i in range(1, len(board), 3):
                for j in range(1, len(board), 3):
                    new = [board[i-1][j-1], board[i][j-1], board[i+1][j-1], board[i-1][j], board[i][j], board[i+1][j], board[i-1][j+1], board[i][j+1], board[i+1][j+1]]
                    if not(validateNumbers(new, "Box")):
                        valid = False
            return valid

        def validateNumbers(sequence, topic):
            valid = True
            for i in range(len(sequence)):
                if sequence.count(sequence[i]) > 1 and sequence[i] != ".":
                    valid = False
                    print(sequence, sequence[i], "falsified")

                if not sequence[i] == ".":
                        print(sequence[i], sequence)

            # print(f'{topic} determined to be {valid}')
            # print(f'Current Sequence: {sequence}\n')
            
            return valid

        print("Valid Rows: ", validateRow())
        print("Valid Columns: ", validateColumn())
        print("Valid Boxes: ", validateBox())
        return validateRow() and validateColumn() and validateBox()

                