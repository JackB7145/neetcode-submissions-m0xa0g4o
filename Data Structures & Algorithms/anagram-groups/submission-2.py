class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            key = [0]*26
            for c in word:
                key[ord(c)-ord('a')] += 1
            key = tuple(key)
            if key not in mp:
                mp[key] = []
            mp[key].append(word)

        res = []
        for l in mp.values():
            res.append(l)

        return res