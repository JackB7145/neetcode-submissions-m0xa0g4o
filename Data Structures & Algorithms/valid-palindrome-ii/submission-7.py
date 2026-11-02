class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for idx in range(len(s)):
            word = s[:idx] + s[idx+1:]
            if word == word[::-1]:
                return True
        return False