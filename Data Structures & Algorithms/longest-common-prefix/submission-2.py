class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)
        print(prefix)
        for i in range(len(strs)):
            string = strs[i]
            if string == prefix:
                continue
            print('current string: ', string)
            while string != prefix:
                print(f'Comparing {string} and {prefix}')
                string = string[:-1]
                if len(string) < len(prefix):
                    prefix = prefix[:-1]

        return prefix