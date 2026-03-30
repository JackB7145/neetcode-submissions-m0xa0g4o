class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for c in s:
            index[c] = 1 + index.get(c, 0)

        def validateSubstring(string):
            flag = True
            for c in string:
                if index[c]:
                    flag = False
                    break
            return flag

        print(index)
        res = []
        substring = []
        for c in s:
            substring.append(c)
            index[c] -= 1
            if not index[c]:
                if validateSubstring(substring):
                    res.append(len(substring))
                    substring = []

        return res
