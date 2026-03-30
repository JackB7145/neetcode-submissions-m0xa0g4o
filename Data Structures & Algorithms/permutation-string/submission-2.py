class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Count charcters of s1, then iterates of size of s1 in s2, looking for the same count
        '''

        if len(s1) > len(s2):
            return False

        mp1 = {}
        for c in s1:
            mp1[c] = mp1.get(c, 0) + 1
        
        n = sum(mp1.values())

        mp2 = {}

        l = 0
        for r in range(len(s2)):
            mp2[s2[r]] = mp2.get(s2[r], 0) + 1
            if r-l+1 > n:
                mp2[s2[l]] -= 1
                if mp2[s2[l]] < 1:
                    del mp2[s2[l]]
                l += 1
            
            if mp2 == mp1:
                return True
        return False            

        