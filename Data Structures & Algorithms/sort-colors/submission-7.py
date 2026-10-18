class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
        
        idx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx -= 1
        
        