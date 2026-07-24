class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        def traverse(idx, curr):
            if idx >= len(nums):
                return curr
            
            return traverse(idx+1, curr ^ nums[idx]) + traverse(idx+1, curr)

        return traverse(0, 0)
