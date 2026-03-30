class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        sides = [0] * k
        if sum(nums) % k != 0:
            return False
        
        length = sum(nums) / k

        def traverse(i):
            nonlocal length
            if i == len(nums):
                return True
            
            for side in range(len(sides)):
                if nums[i] + sides[side] <= length:
                    sides[side] += nums[i]
                    if traverse(i+1):
                        return True
                    
                    sides[side] -= nums[i]

                if sides[side] == 0:
                    break
            return False

        return traverse(0)
