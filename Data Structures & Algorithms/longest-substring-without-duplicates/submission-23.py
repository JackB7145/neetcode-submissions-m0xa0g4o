class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0 
        for c in s:
            if c in seen:
                res = max(res, len(seen))
                seen = set()
            seen.add(c)
        
        return res