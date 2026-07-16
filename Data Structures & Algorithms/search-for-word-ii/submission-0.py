from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        rows, cols = len(board), len(board[0])
        res = set()

        def traverse(i, j, curr, path):
            # bounds + visited check
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return

            char = board[i][j]

            # visited OR not in trie → stop
            if char == "#" or char not in curr.children:
                return

            curr = curr.children[char]
            path += char

            if curr.isWord:
                res.add(path)

            # mark visited
            board[i][j] = "#"

            # explore neighbors
            traverse(i+1, j, curr, path)
            traverse(i-1, j, curr, path)
            traverse(i, j+1, curr, path)
            traverse(i, j-1, curr, path)

            # unmark (backtrack)
            board[i][j] = char

        for i in range(rows):
            for j in range(cols):
                traverse(i, j, trie.root, "")

        return list(res)