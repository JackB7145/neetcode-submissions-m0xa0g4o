from functools import lru_cache

class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        trie = PrefixTree()
        for word in dictionary:
            trie.insert(word)

        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return 0

            # Option 1: treat s[i] as extra
            res = 1 + dfs(i + 1)

            # Option 2: try matching dictionary words via trie
            curr = trie.root
            j = i

            while j < len(s) and s[j] in curr.children:
                curr = curr.children[s[j]]
                j += 1

                if curr.isEnd:
                    res = min(res, dfs(j))

            return res

        return dfs(0)