class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        '''
        1 - 26 Is covered

        next is 26 ^ 1
        '''

        res = ""

        power = 0

        while columnNumber // 26 ** power != 0:
            power += 1

        power -= 1
        
        while columnNumber:
            
            char = chr(ord('A') + columnNumber // 26 ** power - 1)
            columnNumber %= 26 ** power

            res += char

            power -= 1
        
        return res


