class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def traverse(i, j, idx):
            if (i, j) in seen or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            if board[i][j] == word[idx] and idx == len(word)-1:
                return True

            seen.add((i, j))
            
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = False

            for dx, dy in dirs:
                res = res or traverse(i+dx, j+dy, idx+1)
            
            seen.remove((i, j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if traverse(i, j, 0):
                    return True
        
        return False
            
            