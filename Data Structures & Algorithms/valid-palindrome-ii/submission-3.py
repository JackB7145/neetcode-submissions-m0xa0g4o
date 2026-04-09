class Solution:
    def validPalindrome(self, s: str) -> bool:

        def valid(l, r, skip):
            if r <= l + 1:
                return True
            elif s[l] != s[r] and skip:
                return False
            elif s[l] != s[r]:
                return valid(l+1, r, True) or valid(l, r - 1, True)
            return valid(l+1, r-1, False)
        
        left, right = 0, len(s)-1

        return valid(left, right, False)