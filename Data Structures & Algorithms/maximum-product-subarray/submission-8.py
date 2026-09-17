class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            candidates = (n, curMax * n, curMin * n)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res, curMax)

        return res