class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        Do the tabulation approach

        store 3 vars

        move them down when I go up

        do some edge case checks, should be good

        '''

        if n < 3:
            return [0, 1, 1][n]
        
        first, second, third = [0, 1, 1]

        for i in range(2, n):
            curr = first + second + third
            first = second
            second = third
            third = curr

        return third