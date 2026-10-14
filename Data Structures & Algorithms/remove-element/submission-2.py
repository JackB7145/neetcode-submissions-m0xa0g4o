class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for r in range(len(nums)):
            nums[idx] = nums[r]
            if nums[r] != val:
                idx += 1

        return idx