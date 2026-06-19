class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = Counter(s1)
        mp = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                mp[s2[l]] -= 1
                if mp[s2[l]] == 0:
                    del mp[s2[l]]
                l += 1

            mp[s2[r]] += 1
            if mp == key:
                return True
        
        return False