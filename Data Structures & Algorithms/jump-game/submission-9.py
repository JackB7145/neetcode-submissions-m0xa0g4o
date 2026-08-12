class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]

        if len(nums) == 1:
            return True
            
        if nums[0] == 0:
            return False

        for i in range(1, len(nums)):
            jumps = max(jumps-1, nums[i])
            if i + jumps >= len(nums)-1:
                return True
            if not jumps:
                return False
        