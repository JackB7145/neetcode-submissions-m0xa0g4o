class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            n = target-nums[i]
            if n in mp:
                return [mp[n], i]
            
            mp[nums[i]] = i
        return -1