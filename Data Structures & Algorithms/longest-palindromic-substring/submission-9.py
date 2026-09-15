class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0] if s else ""

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                substring = s[i:j+1]

                if len(substring) > len(res) and substring == substring[::-1]:
                    res = substring

        return res
