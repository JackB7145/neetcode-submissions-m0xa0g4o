class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        Brute force with memo?

        choose itself or move on until its greater than 4

        we could keep track of 

        the total and whether or not it had a member that made it



        '''

        memo = {}

        res = 0

        def dfs(curr):
            nonlocal res

            if curr > target:
                return 0
            
            elif curr == target:
                return 1
            
            elif curr in memo:
                return memo[curr]
            
            result = 0
            for i in range(len(nums)):
                result += dfs(curr+nums[i])
            
            memo[curr] = result
            return memo[curr]

        return dfs(0)




        

