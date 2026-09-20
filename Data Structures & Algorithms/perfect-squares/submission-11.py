class Solution:
    def numSquares(self, n: int) -> int:

        squares = [
            i ** 2
            for i in range(int(n ** 0.5), 0, -1)
        ]

        memo = {}

        def dfs(remaining):

            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            minimum = float("inf")

            for square in squares:

                if square > remaining:
                    continue

                minimum = min(
                    minimum,
                    1 + dfs(remaining - square)
                )

            memo[remaining] = minimum

            return minimum

        return dfs(n)
