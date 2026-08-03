class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        sequence = []
        wordSet = set(wordDict)

        def traverse(idx):
            if idx >= len(s):
                res.append(' '.join(sequence[:]))
                return
            
            string = ""
            for i in range(idx, len(s)):
                string += s[i]
                if string in wordSet:
                    sequence.append(string)
                    traverse(i+1)
                    sequence.pop()

        traverse(0)
        return res

        

