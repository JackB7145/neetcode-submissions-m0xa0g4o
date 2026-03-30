class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = [] 
        words = set(wordDict)
        curr = []
        def dfs(i):
            nonlocal res
            if i >= len(s):
                res.append(" ".join(curr[:]))
                return
            
            for idx in range(i, len(s)):
                word = s[i:idx+1]
                if word in words:
                    curr.append(word)
                    dfs(idx+1,)
                    curr.pop()

        dfs(0)
        return res