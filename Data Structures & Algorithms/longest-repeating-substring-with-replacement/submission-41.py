class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        We can use a hashmap to know the amount of characters in the window 

        as we iterate over we want to ensure that the character at l is the target character, and extend as long as its the same or our aloowance <= k

        We can keep track of the count, and we know we need to move forward when (the length of the window) - the left count >= k
        '''
        l = 0
        mp = defaultdict(int)
        res = 0
        for r in range(len(s)):
            mp[s[r]] += 1

            length = r - l + 1
            issues = length - mp[s[l]]
            if issues > k:
                mp[s[l]] -= 1
                l += 1
            
            print(s[l], mp[l], r-l+1)
            res = max(res, min(mp[s[l]] + k, len(s)))
        
        for key in mp:
            res = max(res, mp[key] + k)
        return res