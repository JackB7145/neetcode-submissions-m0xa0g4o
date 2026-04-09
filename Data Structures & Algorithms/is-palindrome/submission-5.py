class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s)-1
        s.lower()
        while leftPointer < rightPointer:
            
            leftChar = s[leftPointer]
            rightChar = s[rightPointer]
            

            if leftChar != rightChar:
                return False

            leftPointer += 1
            rightPointer -= 1
        return True