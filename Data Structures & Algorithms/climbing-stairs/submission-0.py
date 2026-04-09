class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1:

        1

        Res = 1

        2:

        1 1 
        2

        Res = 2

        3:

        111
        21
        12

        Res = 3

        4:

        1111
        112
        121
        22
        211

        Res = 5

        this is a classic fibonacci series

        The numbers of ways we can make it to step n, is the sum of step n-1, n-2
        '''

        num1 = 1
        num2 = 2

        if n in [1, 2]:
            return [num1, num2][n-1]

        for i in range(3, n):
            total = num1 + num2
            if i % 2 == 0:
                num1 = total
            else:
                num2 = total

        return num1+num2