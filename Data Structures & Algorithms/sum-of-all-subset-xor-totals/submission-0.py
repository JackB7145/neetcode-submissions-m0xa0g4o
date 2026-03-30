class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def traverse(idx, total):
            nonlocal res
            if idx >= len(nums):
                res += total
                return
            
            traverse(idx+1, total^nums[idx])
            traverse(idx+1, total)
        
        traverse(0, 0)
        return res
            
