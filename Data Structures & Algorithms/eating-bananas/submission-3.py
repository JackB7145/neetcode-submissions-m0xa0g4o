class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        speed = 0
        b = piles.copy()
        print(b)
        while b[-1] > 0:
            speed += 1
            index = 0
            b = piles.copy()
            for i in range(h):
                b[index]-=speed
                if b[index] <= 0:
                    index += 1
                    if index == len(b):
                        return speed
        return speed
            
                
            
            
