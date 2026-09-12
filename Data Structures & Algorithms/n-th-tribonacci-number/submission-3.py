class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        theory:

        T0 + T1 + T2 = T3

        T0 = 0 
        T1 = 1
        T2 = 

        '''

        if n < 3:
            return [0, 1, 1][n]

        one, two, three = 1, 1, 0

        for i in range(2, n):
            temp = one

            one = one + two + three

            three = two
            two = temp

        return one


        