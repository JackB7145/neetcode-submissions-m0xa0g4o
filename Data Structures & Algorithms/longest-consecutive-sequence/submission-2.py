class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 not in nums:
                temp = n
                count = 0
                while temp in nums:
                    temp+=1
                    count += 1
                res = max(res, count)
        return res
