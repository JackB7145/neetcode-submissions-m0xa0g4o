class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            for j in range(minJump, maxJump + 1):
                if i + j >= len(s):
                    break

                if s[i + j] == '0':
                    dp[i + j] = True

        return dp[-1]