class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        largest = max(nums)
        total = nums[0]
        lastIdx = 0
        for i in range(1, len(nums)):
            if total <= total + nums[i] and total >= 0:
                total += nums[i]
            else:
                total = nums[i]
                lastIdx = i
            
            largest = max(largest, total)

        cnt = 0
        print(total, lastIdx)

        while cnt < lastIdx:
            total += nums[cnt]
            cnt += 1
            largest = max(largest, total)

        return largest        

        