class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        In the method, subtract and add each number, keeping track of the index and the sum in state???????

        cache that, top down dp?
        ''' 

        cache = {}

        def go(idx, total):
            if idx >= len(nums) and total == target:
                return 1
            
            elif idx >= len(nums):
                return 0

            elif (idx, total) in cache:
                return cache[(idx, total)]
                

            res = go(idx+1, total+nums[idx]) + go(idx+1, total-nums[idx])

            cache[(idx, total)] = res

            return res
        
        return go(0, 0)
