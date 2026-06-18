class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        mp = defaultdict(int)
        l = 0
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            mp[s[r]] += 1
            maxFreq = max(maxFreq, mp[s[r]])

            if (r - l + 1) - maxFreq > k:
                mp[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res