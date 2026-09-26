class Solution:
    def reverse(self, x: int) -> int:

        neg = -1 if x < 0 else 1

        if neg < 0:
            x*=-1

        temp = 0

        power = 1
        while x:
            digit = x % 10
            x //= 10

            temp *= 10
            temp += digit 

        return neg*temp if -2**31 <= neg*temp <= 2**31-1 else 0
