class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        So we can have 2 instances here of calculating the size of a histogram

        There is min of heights // distance of the two. Kinda like 2 pointer

        But you can also pick just the one itself


        If we are using a stack, when can we forget information

        when we've included it in our maximum?

        I feel like this is two pointer, but it's not there is something I'm missing in the question


        If we had two pointers where we started from either side, when would we move left vs right? 
        If we move the smaller one, we calculate and move, if we move the larger one we calculate and then move, but what if there is a recangle that can be formed with that one


        Do we add the items in a stack, and when we find a value that is. No. I don't know.

        Sub optiaml is horizontally scanning elft from right from every start ooint

        '''
        res = 0 
        for i in range(len(heights)):
            smallestHeight = heights[i]
            for j in range(i, len(heights)):
                smallestHeight = min(smallestHeight, heights[j])
                res = max(res, smallestHeight * (j - i + 1))

        return res
