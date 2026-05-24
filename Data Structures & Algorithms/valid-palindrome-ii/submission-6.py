class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(word):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return isValid(s[l+1:r+1]) or isValid(s[l:r])

            l += 1
            r -= 1
        return True