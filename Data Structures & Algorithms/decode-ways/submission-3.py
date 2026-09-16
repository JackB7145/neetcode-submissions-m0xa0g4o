class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for i in range(1, len(s)):
            # Decode s[i] as a single digit
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # Decode s[i-1:i+1] as a two-digit number
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]

        return dp[-1]
