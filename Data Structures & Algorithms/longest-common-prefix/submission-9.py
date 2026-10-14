class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for idx in range(len(min(strs))):
            c = strs[0][idx]
            for word in strs:
                char = word[idx]
                if char != c:
                    return prefix

            prefix+=c

        return prefix

