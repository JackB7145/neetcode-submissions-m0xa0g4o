class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        def backtrack(idx): 
            if idx >= len(nums):
                res.append(temp[:])
                return

            temp.append(nums[idx])
            backtrack(idx+1)
            temp.pop()

            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1

            backtrack(idx+1)
        
        backtrack(0)
        return res
