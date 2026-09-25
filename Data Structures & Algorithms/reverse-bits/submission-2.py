class Solution:
    def reverseBits(self, n: int) -> int:
        newNumber = 0
        for _ in range(32):
            bit = n & 1
            n >>= 1
            newNumber |= bit
            newNumber <<= 1
        
        return newNumber >> 1
