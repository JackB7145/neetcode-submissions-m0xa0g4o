class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        res = float('inf')
        words = set(wordList)
    
        def traverse(curr, cnt):
            nonlocal res
            if curr in visited:
                return

            if curr == endWord:
                res = min(res, cnt)
                return

            visited.add(curr)
            for i in range(len(curr)):
                for char in range(97, 123):
                    possibleWord = curr[:i] + chr(char) + curr[i+1:]
                    if possibleWord in words:
                        traverse(possibleWord, cnt+1)
                
        traverse(beginWord, 1)
        if res >= float('inf'):
            return 0
        return res
                        

