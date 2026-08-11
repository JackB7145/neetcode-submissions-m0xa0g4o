class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -10**9
        total = 0
        for n in nums:
            total = max(total+n, n)
            res = max(res, total)

        return res