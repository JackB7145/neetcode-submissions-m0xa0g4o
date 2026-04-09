class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #This is a sliding window problem. 
        #The principle of sliding window is that, 
        #For every iteration we calculate what we need
        #But as we iterate we just make the changes to the calculation
        #Based on the newly introduced index and the lost index
        #However, the bounds of teh sliding window don;t have to change
        #Due to iteration, it could be by another condition

        #In this problem the calculation we perform is teh size of the new array
        #As we iterate through the string we will have a lB and a rB
        #Left bound and right bound
        #If we encounter a letter we already have we compute the region as in get the max, 
        #Then after that we move lB to the rB and restart the process from i + 1
        if not s:
            return 0
        lB = 0
        maxChar = 1
        temp = s[lB]
        for i in range(0, len(s)):
        
            if s[i] not in temp:
                temp += s[i]
            
            else:
                maxChar = max(maxChar, len(temp))
                lB += 1
                temp = temp[1:]
                temp+=s[i]
                print(f'temp: {temp}')
        
        maxChar = max(maxChar, len(temp))

        print(temp)
        return maxChar
            
            
