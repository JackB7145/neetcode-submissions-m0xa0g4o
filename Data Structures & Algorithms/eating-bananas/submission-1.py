class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        speed = 0
        while True:
            speed += 1
            index = 0
            b = piles.copy()
            for i in range(h):
                b[index]-=speed
                if b[index] <= 0:
                    index += 1
                    if index == len(b):
                        return speed
            if b[-1] < 1:
                return speed
            
                
            
            
