class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set('abcdefghijklmnopqrstuvwxyz1234567890')
        s = s.lower().replace(" ", '')
        s = ''.join([c for c in s if c in valid])

        return s[::-1] == s
