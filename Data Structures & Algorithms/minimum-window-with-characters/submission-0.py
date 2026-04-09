class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        lettersIndex = defaultdict(int)
        for char in t:
            letters[char] += 1
        lB = 0
        for i in range(len(t)-1, len(s)):
            lettersIndex[s[i]] += 1
            res = False
            for key in letters:
                if letters[key] == lettersIndex[key] and i - lB + 1 >= len(s):
                    res = True
            if res:
                return s[lB:i]

            while i - lB + 1 > len(s) and s[lB] not in letters:
                lettersIndex[s[lB]] -= 1
                lB += 1
        return ""