class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = False
        def traverse(i, j, idx):
            nonlocal flag

            if idx >= len(word):
                flag = True
                return 

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or flag:
                return
            
            traverse(i+1, j, idx+1)
            traverse(i-1, j, idx+1)
            traverse(i, j+1, idx+1)
            traverse(i, j-1, idx+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                traverse(i, j, 0)
            
        return flag
            

            
