class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        def dfs(num):
            if num in dp:
                return dp[num]

            # initialize local variable for max product
            split_product = 0 if num == n else num  # can't take n itself as a piece
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                if val > split_product:
                    split_product = val

            dp[num] = split_product
            return dp[num]

        return dfs(n)