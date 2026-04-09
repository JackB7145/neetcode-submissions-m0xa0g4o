class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(1, len(s)):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i - 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]


        '''
        We make a giant array of all the possible substrings from i to j

        so all the substrings s[0:...n], s[1:..n] and so on and so forth

        

        
        '''