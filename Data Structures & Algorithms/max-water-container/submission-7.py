class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        def getVolume(l, r):
            return min(heights[l], heights[r]) * (r-l)


        l, r = 0, len(heights)-1

        while l < r:
            res = max(res, getVolume(l, r))
            if heights[l] < heights[r]:
                l += 1

            else:
                r-= 1
        
        return res
        