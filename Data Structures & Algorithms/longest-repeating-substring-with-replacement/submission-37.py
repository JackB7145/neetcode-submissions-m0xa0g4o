class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        We can use a hashmap to know the amount of characters in the window 

        as we iterate over we want to ensure that the character at l is the target character, and extend as long as its the same or our aloowance <= k

        We can keep track of the count, and we know we need to move forward when (the length of the window) - the left count >= k
        '''
        l = 0
        mp = {}
        res = 0
        for r in range(len(s)):
            
            mp[s[r]] = mp.get(s[r], 0) + 1

            issues = (r-l+1) - mp[s[l]]

            while issues > k:
                mp[s[l]] -= 1
                l += 1
                issues = (r-l+1) - mp[s[l]]

            print(s[l], issues)
            length = (r-l+1) + k-issues
            newLength = length if length <= len(s) else len(s)

            res = max(res, newLength)
        
        l += 1 if l < len(s) else 0
        issues = (r-l+1) - mp[s[l]]
        length = (r-l+1) + k-issues
        newLength = length if length <= len(s) else len(s)

        return max(res, newLength)