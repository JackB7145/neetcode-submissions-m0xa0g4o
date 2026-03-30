class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(strs)):
            string = strs[i]
            prefix = prefix[:len(string)]
            while string != prefix:
                string = string[:-1]
                prefix = prefix[:len(string)]
        return prefix
