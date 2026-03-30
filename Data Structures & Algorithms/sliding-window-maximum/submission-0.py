class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        counter = 0
        lB = 0
        for i in range(k-1, len(nums)):
            res[counter] = max(nums[lB:i+1])
            print(res, counter, nums[lB:i+1])
            lB += 1
            counter += 1
            

        return res