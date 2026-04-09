class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        Define a dfs function that accepts totals

        and adds the length to 4 different totals

        if at the end they all equal for any instance we return true

        this works cuz the length of the array is only up to 15

        4 different ways is 4^15 is 1 million operations

        or 1 x 10^7

        that'll work lol
        '''

        def traverse(idx, one, two, three, four):
            if idx >= len(matchsticks):
                return one == two == three == four

            m = matchsticks[idx]

            return traverse(idx+1, one+m, two, three, four) or traverse(idx+1, one, two+m, three, four) or traverse(idx+1, one, two, three+m, four) or traverse(idx+1, one, two, three, four+m)

        return traverse(0, 0, 0, 0, 0)
