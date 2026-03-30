class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax=nums[0]
        globalMax=nums[0]

        for i in range(1,len(nums)):
            localMax = max(localMax+nums[i], nums[i])
            globalMax = max(localMax, globalMax)

        return globalMax