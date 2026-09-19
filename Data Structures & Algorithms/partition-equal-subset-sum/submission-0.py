class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Theory:

        we are looking for where

        sum1 = sum(subset1)
        sum2 = sum(subset2)

        where sum1 == sum2 and sum1 + sum2 = sum(nums)

        so 2x = sum(nums)

        so our target is x = sum(nums)/2

        in our logic, we just need to find a sum that is our target, because then by definition the other sum is the target as well. 

        '''
        total = sum(nums)
        target = total / 2
        if total % 2 != 0:
            return False

        cache = {}
        used = [False] * len(nums)
        def dfs(total):
            if total in cache:
                return cache[total]
            
            if total == target:
                cache[total] = True
                return True
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    if dfs(total + nums[i]):
                        return True
                    
                    used[i] = False
            
            cache[total] = False
            return False
    
        return dfs(0)

                    
                    
            


                    



        
