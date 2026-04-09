class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace("?", "").replace(" ", "").lower()
        print(s, s[len(s)::-1])
        return s == s[len(s)::-1]      