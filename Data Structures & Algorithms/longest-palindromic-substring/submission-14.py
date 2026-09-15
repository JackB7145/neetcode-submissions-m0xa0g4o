class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        memo = [[None] * n for _ in range(n)]
        resIdx, resLen = 0, 1

        def is_pal(i, j):
            if i >= j:
                return True
            if memo[i][j] is not None:
                return memo[i][j]
            result = s[i] == s[j] and (j - i <= 2 or is_pal(i + 1, j - 1))
            memo[i][j] = result
            return result

        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j) and (j - i + 1) > resLen:
                    resIdx, resLen = i, j - i + 1

        return s[resIdx : resIdx + resLen]