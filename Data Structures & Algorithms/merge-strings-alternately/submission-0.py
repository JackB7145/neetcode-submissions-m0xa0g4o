class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        
        print(i)
        if len(word1) == len(word2):
            return ''.join(res)
        elif i+1 >= len(word1):
            return ''.join(res) + word2[i+1:]
        return ''.join(res) + word1[i+1:]