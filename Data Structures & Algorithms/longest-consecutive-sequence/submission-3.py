class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                num = n + 1
                while num in nums:
                    num += 1

                res = max(res, num-n)
        
        return res