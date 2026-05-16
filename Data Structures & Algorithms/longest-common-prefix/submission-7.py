class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, c in enumerate(min(strs)):
            for word in strs:
                if word[i] != c:
                    return res
            res += c
        return res