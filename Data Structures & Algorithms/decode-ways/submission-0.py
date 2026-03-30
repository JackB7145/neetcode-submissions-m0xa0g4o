class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [[0, 0] for _ in range(n)]

        # Base case
        dp[0][0] = 1  # single-digit decode at index 0

        for i in range(1, n):
            # Single digit case
            if s[i] != "0":
                dp[i][0] = dp[i-1][0] + dp[i-1][1]

            # Two digit case (YES, this correctly checks "10")
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i][1] = dp[i-1][0]

        return dp[-1][0] + dp[-1][1]
