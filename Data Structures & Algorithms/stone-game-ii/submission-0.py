class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cache = {}

        def dfs(i, M):
            # No stones left
            if i >= n:
                return 0

            if (i, M) in cache:
                return cache[(i, M)]

            res = float('-inf')
            total = 0

            # Take X stones, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                total += piles[i + X - 1]

                # I gain `total`, then opponent plays optimally.
                res = max(
                    res,
                    total - dfs(i + X, max(M, X))
                )

            cache[(i, M)] = res
            return res

        return (sum(piles) + dfs(0, 1)) // 2
