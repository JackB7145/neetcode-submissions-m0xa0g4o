class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        temp = nums[len(nums)-k:]

        idx = len(nums)-1
        for i in range(len(nums)-k-1, -1, -1):
            nums[idx] = nums[i]
            idx -= 1

        for i in range(k):
            nums[i] = temp[i]

        

