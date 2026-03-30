class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        pos = 0

        for _ in range(32):
            abit = a & 1
            bbit = b & 1

            if carry & abit & bbit:
                bit = 1
                carry = 1
            elif (carry & abit) | (carry & bbit) | (abit & bbit):
                bit = 0
                carry = 1
            elif carry | abit | bbit:
                bit = 1
                carry = 0
            else:
                bit = 0
                carry = 0

            res |= (bit << pos)

            pos += 1
            a >>= 1
            b >>= 1

        if res >= 1 << 31:
            res -= 1 << 32

        return res