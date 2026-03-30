class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, idx):
            if idx >= len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or (i, j) in used:
                return False

            print(i, j, board[i][j])

            used.add((i, j))  

            condition = traverse(i+1, j, idx+1) or traverse(i-1, j, idx+1) or traverse(i, j+1, idx+1) or traverse(i, j-1, idx+1)

            used.remove((i, j))
            
            return condition
        
        used = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if traverse(i, j, 0):
                    return True
        return False
                        

            
