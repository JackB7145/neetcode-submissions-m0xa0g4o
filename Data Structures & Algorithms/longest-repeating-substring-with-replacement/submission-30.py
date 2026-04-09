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

            allowance = (r-l+1)-mp[s[l]]
            if allowance > k:
                res = max(res, mp[s[l]] + k)
                mp[s[l]] -= 1
                l += 1
            
            print(mp, allowance)
            newLength = (r-l+1) + (k-allowance) if (r-l+1) + (k-allowance) <= len(s) else len(s)

            res = max(res, newLength)
        return res