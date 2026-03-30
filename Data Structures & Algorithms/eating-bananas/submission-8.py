class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        The purpose of this question is to show that you
        don't just have to binary search over a dataset but any data with bounds. The bounds are 1, and the maxiumum of the dataset,and the answer k lies inbetween
        If the rate mid isn't able to eat all the bananas in the allocated time
        we increase it, if it is we decrease it. We keep track of the last rate seen
        '''
        def checkRate(rate: int)->int:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
            return hours

        l, r = 1, max(piles)
        lastRate = -1
        while l <= r:
            m = (l+r)//2
            if checkRate(m) <= h:
                lastRate = m
                r = m - 1
            else:
                l = m + 1
        return lastRate

