class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        def calculateArea(indexDifference, one, two):
            smaller = min(one, two)
            print(indexDifference, one, two)
            return indexDifference * smaller

        lP = 0
        rP = len(heights) - 1

        while lP < rP:
            currLeft = heights[lP]
            currRight = heights[rP]

            if currLeft > heights[lP + 1] or currLeft >= currRight:
                area = max(area, calculateArea(rP - lP, currLeft, currRight))
                rP -= 1

            elif currLeft < heights[lP + 1] and currLeft < currRight:
                area = max(area, calculateArea(rP - lP, currLeft, currRight))
                lP += 1
            
        return area
        
















        return area