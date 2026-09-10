class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return [1, 2][n-1]

        first = 2
        second = 1

        for i in range(n-2):
            new = first + second
            second = first
            first = new

        return first

        