class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            string = strs[i]
            print('starting with', string)
            while prefix != string:
                string = string[:-1]
                print('comparing', prefix, 'and', string)
                while len(string) < len(prefix):
                    prefix = prefix[:-1]

        return prefix