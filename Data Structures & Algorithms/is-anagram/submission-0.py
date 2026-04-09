class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for char in s:
            try:
                t.remove(char)
            except:
                pass

        if not(t):
            return True
        return False