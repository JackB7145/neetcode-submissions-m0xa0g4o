class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        
        res = []

        while idx1 < len(word1) and idx2 < len(word2):
            res.append(word1[idx1])
            res.append(word2[idx2])
            idx1 += 1
            idx2 += 1
        
        if idx1 < len(word1):
            res.append(word1[idx1:])
        elif idx2 < len(word2):
            res.append(word2[idx2:])
        
        return ''.join(res)