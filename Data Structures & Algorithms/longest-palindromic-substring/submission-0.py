class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Iterate over every element and treat them like they are the centre of the palendrome

        Go left, and go right until that start isn't. But how can we deal with even 
        lengthed strings and palendromes. Maybe only go one direction? or give 1 skip

        we know we have to do this if the left or right is the same as the centre

        So maybe we check fro this cnodition, and if its true. We Include ours on the side it doesn't have



        '''

        length = 0
        string = ""
        for i in range(len(s)):
            l = i-1
            r = i+1
            if 0 < i and s[i] != s[i-1] and i < len(s)-1 and s[i+1] == s[i]:
                r+=1
            elif 0 < i and s[i] == s[i-1] and i < len(s)-1 and s[i+1] != s[i]:
                l-=1
            
            while 0 < i < len(s)-1 and s[l] == s[r] and l > -1 and r < len(s):
                l -= 1
                r += 1
            
            l += 1
            r -= 1

            length = max(length, r-l+1)
            print(l, r, r-l+1, length)


            if len(string) < length:
                string = s[l:r+1]
        
        return string
            

            

         