class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #My first impression. Given that this is a sliding window question lets break it down:

        #K is the letters of allowance, that can be used to manipulate the longest. The longest should be calculated once the temp k is 0

        #So we should only move the left pointer along when k is 0 
        letters = set()
        letters.add(s[0])
        lB = 0
        maxLength = 0
        temp = k
        for i in range(1, len(s)):
            if not k and s[i] not in letters:
                while s[lB] in letters:
                    lB += 1
                
                letters = set()
                letters.add(s[lB])
                k = temp - (i - lB - temp)

                # lB -= k
                # k = 0
                
                
            maxLength = max(maxLength, i - lB + 1)
            if s[i] not in letters:
                k -= 1

        return maxLength



        #Input: "", k = 3