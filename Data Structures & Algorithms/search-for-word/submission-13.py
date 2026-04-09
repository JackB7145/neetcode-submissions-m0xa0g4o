class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, idx):
            if idx >= len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or (i, j) in used:
                return False

            print(board[i][j])
            used.add((i, j))  

            return traverse(i+1, j, idx+1) or traverse(i-1, j, idx+1) or traverse(i, j+1, idx+1) or traverse(i, j-1, idx+1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                used = set()
                if traverse(i, j, 0):
                    return True
        return False
                        

            
