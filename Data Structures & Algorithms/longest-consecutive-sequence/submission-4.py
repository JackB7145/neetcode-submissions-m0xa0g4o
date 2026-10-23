class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                cnt = 1
                num = n
                while num in nums:
                    res = max(res, cnt)
                    cnt += 1
                    num += 1
        
        return res