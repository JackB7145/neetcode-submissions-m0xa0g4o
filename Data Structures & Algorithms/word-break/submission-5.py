class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def traverse(idx):
            if idx in memo:
                return memo[idx]
            if idx == len(s):
                return True

            for i in range(idx, len(s)):
                if s[idx:i+1] in wordSet and traverse(i + 1):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False

        return traverse(0)
