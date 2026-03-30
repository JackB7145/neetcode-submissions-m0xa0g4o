class Solution:
    def countBits(self, n: int) -> List[int]:
        def cntBits(number: int)->int:
            cnt = 0
            while number:
                if number & 1:
                    cnt += 1
                number >>= 1
            return cnt

        res = []
        for i in range(n+1):
            res.append(cntBits(i))
        
        return res