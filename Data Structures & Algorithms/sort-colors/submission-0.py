class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        This is the flag prob where we keep a left and right pointer, and move all 1 color
        to the left, and all 1 color to the right. whats left is the middle. 
        '''

        red, blue = 0, len(nums)-1
        l, r = 0, len(nums)-1
        while l < len(nums):
            if nums[l] == 0:
                nums[l], nums[red] = nums[red], nums[l]
                red += 1
            if nums[r] == 2:
                nums[r], nums[blue], nums[blue], nums[r]
                blue -= 1

            l += 1
            r -= 1
        
        
        