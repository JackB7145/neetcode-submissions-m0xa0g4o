class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        skip = False
        while l < r:
            if s[l] != s[r] and skip:
                return False
            elif s[l] != s[r]:
                if s[l] == s[r-1]:
                    r -= 1
                else:
                    l += 1
                skip = True
                continue
            
            l += 1
            r -= 1
        return True

        