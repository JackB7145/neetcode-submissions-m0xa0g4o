class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * len(s)
        words = set(wordDict)

        def dfs(i):
            if i >= len(s):
                return True
            
            if dp[i] is not None:
                return dp[i]
            
            res = False
            string = ""
            for idx in range(i, len(s)):
                string += s[idx]
                if string in words:
                    if dfs(idx+1):
                        return True
            
            dp[i] = res
            return res
        
        return dfs(0)
