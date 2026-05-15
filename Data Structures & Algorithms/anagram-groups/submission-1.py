class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for string in strs:
            ords = [0 for _ in range(26)]
            for c in string:
                ords[ord(c)-ord('a')] += 1

            mp[tuple(ords)].append(string)
        
        return list(mp.values())