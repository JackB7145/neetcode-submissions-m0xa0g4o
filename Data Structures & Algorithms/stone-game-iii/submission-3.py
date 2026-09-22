class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = [None for _ in range(len(stoneValue))]


        def dfs(i):
            if i >= len(stoneValue):
                return 0

            if cache[i] is not None:
                return cache[i]

            best = float("-inf")
            take = 0

            for k in range(3):
                if i + k < len(stoneValue):
                    take += stoneValue[i + k]

                    # I take these stones,
                    # then the other player gets to play.
                    best = max(
                        best,
                        take - dfs(i + k + 1)
                    )

            cache[i] = best
            return best

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
