class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, idx):
            if idx >= len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            
            return traverse(i+1, j, idx+1) or traverse(i-1, j, idx+1) or traverse(i, j+1, idx+1) or traverse(i, j-1, idx+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], board[i][j] != word[0], word[0])
                if traverse(i, j, 0):
                    print(i, j, board[i][j])
                    return True
        return False
                        

            
