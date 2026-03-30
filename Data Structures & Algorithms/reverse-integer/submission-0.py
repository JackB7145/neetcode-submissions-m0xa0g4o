class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1

        if not -2**31 <= x <= 2**31 - 1:
            return 0

        x = str(abs(x))

        x = neg*int(x[::-1])

        if not -2**31 <= x <= 2**31 - 1:
            return 0
        return x

