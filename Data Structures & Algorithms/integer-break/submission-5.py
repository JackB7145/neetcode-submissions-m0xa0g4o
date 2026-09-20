class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        So this shoukd be the same logic as the last solution

        we have 2 properties we want to maintain 

        the value of dp si that we can break it up into subproblems

        and keep track of the remaining like we did the last one

        we provide n and for each n, we choose any number greater than 2

        keep track of the maximum product, returning the product each time
        '''

        cache = {} #remaining: maxProduct

        def dfs(remaining):
            if remaining == 0:
                return 1
            
            elif remaining in cache:
                return cache[remaining]
            
            elif remaining < 0:
                return 0

            res = -1e9

            for i in range(1, n+1):
                if i == n:
                    continue
                res = max(res, i * dfs(remaining-i))
            
            cache[remaining] = res
            return res

        return dfs(n)