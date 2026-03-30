# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         '''
#         So we can have 2 instances here of calculating the size of a histogram

#         There is min of heights // distance of the two. Kinda like 2 pointer

#         But you can also pick just the one itself


#         If we are using a stack, when can we forget information

#         when we've included it in our maximum?

#         I feel like this is two pointer, but it's not there is something I'm missing in the question


#         If we had two pointers where we started from either side, when would we move left vs right? 
#         If we move the smaller one, we calculate and move, if we move the larger one we calculate and then move, but what if there is a recangle that can be formed with that one


#         Do we add the items in a stack, and when we find a value that is. No. I don't know.

#         Sub optiaml is horizontally scanning elft from right from every start ooint

#         '''
#         res = 0 
#         for i in range(len(heights)):
#             smallestHeight = heights[i]
#             for j in range(i, len(heights)):
#                 smallestHeight = min(smallestHeight, heights[j])
#                 res = max(res, smallestHeight * (j - i + 1))

#         return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #Moving the start back for eventual lagging the current start back
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


'''
You keep track of a monoatomic increasing stack to ensure that every height at height[i] only has heights larger than it after, and smaller than it prior (Meaning before it, it'snot going to be the bottle neck, and after it it is.)

You pop from the increasing stack when you find a height that will be a bottle neck keeping track of the start and end indexes. As you pop, you calculate the maximum height that height[i] provided by finding the difference between the start
and current position. Then, when you are done, the end positon becomes the new start position of the current bottleneck given that it can extend backwarsd. 

This is to ensure the logic that each height can only extend forward, which is important for solving the problem in o(n)
'''
