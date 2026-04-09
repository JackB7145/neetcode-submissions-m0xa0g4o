class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower().replace('?', '').replace("'", '').replace('.', '').replace('!', '').replace(" ", '').replace(',', '')
        print(s)
        leftPointer = 0
        rightPointer = len(s)-1
        while leftPointer < rightPointer:
            leftChar = s[leftPointer]
            rightChar = s[rightPointer]

            if leftChar != rightChar:
                return False
            
            leftPointer += 1
            rightPointer -= 1
        return True