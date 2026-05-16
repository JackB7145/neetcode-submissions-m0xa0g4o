class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            brk = False
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    brk = True
            if brk:
                break
            res += strs[0][i]

        return res
