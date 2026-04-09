class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        In the hint, it says to image an array size 2, and then think about of size 3

        See a patturn?

        e.g.

        [2, 5]

        the answer is 10 since 5 x 2 = 10

        [2, -1, 5]

        I don't know, lets see if I can abuse memoization in top down dp

        we have a recursive function that keeps track of the product at each step of choosing either to remove the last used element from the product

        or continuing on to the next. That's just using recursion instead of iteration

        nah I still don't know how to do this, I just don't understand the algorithm I need to implement. Suposedly gained from the example above
        '''

        res = 0
        high = nums[0]
        low = nums[0]
        for i in range(1, len(nums)):
            temp = high
            high = max(high*nums[i], low*nums[i], nums[i])
            low = min(temp*nums[i], low*nums[i], nums[i])
            res = max(high, low)
        
        return res