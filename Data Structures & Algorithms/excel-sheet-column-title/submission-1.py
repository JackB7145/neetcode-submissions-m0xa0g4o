class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = ""

        while columnNumber > 0:

            columnNumber -= 1

            mod = columnNumber % 26
            char = chr(ord('A') + mod)

            res = char + res

            columnNumber //= 26

        return res