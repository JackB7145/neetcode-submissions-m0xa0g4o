class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        A rotated sorted array means it's been rotated k times about the pivot
        I think, given that it is still sorted, we can look for the sorted portion first, check if our target is in between 
        the sorted portion and then move over to the unsorted portion. We have 2 decion poiints or paths::

        1. If left <= target <= mid -> Move right pointer
        2. If mid <= target <= right -> Move left pointer

        If mid is target: return the index right? Lets try that
        '''

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            left, mid, right = nums[l], nums[m], nums[r]
            if mid == target:
                return m
            elif left <= target <= mid:
                r = m - 1
            else:
                l = m + 1

        return -1