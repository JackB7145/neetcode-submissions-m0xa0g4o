from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    # Swap adjacent elements if out of order
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
