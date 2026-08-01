class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        limit = total // 4
        matchsticks.sort(reverse=True)

        sides = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[idx] > limit:
                    continue
                
                if i > 0 and sides[i] == sides[i - 1]:
                    continue
                
                sides[i] += matchsticks[idx]
                if dfs(idx + 1):
                    return True
                sides[i] -= matchsticks[idx]
            
            return False

        return dfs(0)