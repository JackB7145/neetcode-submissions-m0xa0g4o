class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dp(i, j):
            if i > j:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            # Take left:
            # I gain piles[i], then the other player gets to play.
            take_left = piles[i] - dp(i + 1, j)

            # Take right:
            take_right = piles[j] - dp(i, j - 1)

            cache[(i, j)] = max(take_left, take_right)
            return cache[(i, j)]

        return dp(0, len(piles) - 1) > 0
