class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        It's circular, but the algo should still stand, the only thing we have to wrry about
        is the end

        I could do the linear solution starting from every place omitting the end, but that would be worse case n**2
        
        perhaps start from the maximum. Since we can ommit the end and we know we won't be losing anything
        '''

        if len(nums) == 1:
            return nums[0]
            
        highest = max(nums)
        idx = nums.index(highest)

        nums = nums[idx:]+nums[:idx]
    
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)-1):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr

        return curr
