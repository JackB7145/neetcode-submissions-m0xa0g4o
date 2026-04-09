class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Recursive function consisting of choosing to space, or not to space and continue on. 

        Memoized by word, and whether or not it leads to a valid solution

        '''

        def traverse(idx):
            if idx == len(s):
                return True
            
            curr = ""
            for i in range(idx, len(s)):
                curr += s[i]
                if curr in wordDict:
                    res = traverse(i+1)
                    if res:
                        return True
        
            return False
        
        return traverse(0)