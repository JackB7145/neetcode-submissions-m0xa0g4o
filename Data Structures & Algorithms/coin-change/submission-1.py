class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cnt = 0
        coins.sort()
        for i in range(len(coins)-1, -1, -1):
            cnt += amount // coins[i]
            amount %= coins[i]
        
        return cnt if amount == 0 else -1