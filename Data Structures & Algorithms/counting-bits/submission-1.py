class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            temp = 0
            while num:
                if num & 1:
                    temp += 1
                num >>= 1
            return temp
        
        res = []
        for i in range(n+1):
            res.append(count(i))
        
        return res