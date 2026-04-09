from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        rB = nums[0]
        lB = 0
        longestJump = nums[0]
        while rB < len(nums) - 1:
            print(longestJump)
            if rB >= lB:
                longestJump = max(longestJump, nums[lB]+lB)
                lB += 1
            else:
                rB = longestJump
                jumps += 1
        
        return jumps + 1