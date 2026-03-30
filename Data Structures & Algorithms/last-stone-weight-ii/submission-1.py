from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}

        def dfs(i, diff):
            if i == len(stones):
                return abs(diff)

            if (i, diff) in dp:
                return dp[(i, diff)]

            add = dfs(i + 1, diff + stones[i])
            subtract = dfs(i + 1, diff - stones[i])

            dp[(i, diff)] = min(add, subtract)
            return dp[(i, diff)]

        return dfs(0, 0)