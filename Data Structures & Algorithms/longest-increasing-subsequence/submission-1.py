class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        If I wanted to do this in n**2 time

        I would do a linear scan from every position and see how many are greater

        and then return the max

        that doesn't work because just becayse we take the  next biggest one, doesnt't mean its the best

        take [1, 4, 2, 3] the answer is 3, but with that technique we will never get [1, 2, 3] in our subsequence

        because from every starting point, there are multiple bests. 

        what we could do is call the function over every starting point, and keep track of or cache the largest from each startign point

        and then retrun the max
        '''

        dp = [None] * len(nums)
        
        def dfs(idx):
            if dp[idx] != None:
                return dp[idx]
            
            if idx >= len(dp):
                return 0

            res = 1
            for i in range(idx+1, len(dp)):
                if nums[i] > nums[idx]:
                    res = max(res, 1 + dfs(i))

            dp[idx] = res
            return res

        for i in range(len(dp)):
            dfs(i)

        return max(dp)