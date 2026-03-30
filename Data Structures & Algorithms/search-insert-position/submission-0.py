class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        high = len(nums)
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                high = m
                r = m - 1
            else:
                l = m + 1
        return high
                