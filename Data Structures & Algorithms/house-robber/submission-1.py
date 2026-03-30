class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        At every step you have to decide whether you take the n-1 house
        or the n-2 house but not both

        So we start at the base of the street

        we choose either this one, or the next one.

        If we choose this one or the next one, it determines whether we get the one after that 

        one = 1st house
        two = 2nd house

        Say we go to the third house. 

        We should do one and the third, now to make then 2nd, and repeat making one the previous 2nd

        But this results in an every other mentality which we dont want.

        What if it was better to do the first house, and the 4th house than to do the 2nd and the first house

        an example like

        [5, 0, 0, 5]

        reveals this. The answer is 10

        But with our current algorithm we would get 5

        Okay new algo structure. If we want this current one, we can't have the one behind it

        or, if we want the current one, we can't have the next one

        two variables, two holds the most recent, one holds

        the previous best decision

        if the current one is greater than the next. We do one + the current and swap one and two, else, we set one to be the max of the two
        '''

        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for n in nums:
            curr = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = curr

        return prev1

