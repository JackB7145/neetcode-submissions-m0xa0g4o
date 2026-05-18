class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[reds], nums[i] = nums[i], nums[reds]
                reds += 1

        whites = reds
        print(nums, reds)
        for i in range(reds, len(nums)):
            if nums[i] == 1:
                nums[whites], nums[i] = nums[i], nums[whites]
                whites += 1
