class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            res ^= i
            res ^= nums[i]

        res ^= len(nums)
        
        return res