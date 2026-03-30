from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, index, visited):
            if index == len(word):
                return True
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                (i, j) in visited or board[i][j] != word[index]):
                return False

            visited.add((i, j))
            found = (
                dfs(i+1, j, index+1, visited) or
                dfs(i-1, j, index+1, visited) or
                dfs(i, j+1, index+1, visited) or
                dfs(i, j-1, index+1, visited)
            )
            visited.remove((i, j))  # backtrack
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False
