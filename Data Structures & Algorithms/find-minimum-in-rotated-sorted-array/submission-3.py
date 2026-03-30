class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        The premise of this question is understanding rotations. 

        The minimum in a stored array will be at the left most index

        In a rotated sorted array we just need to locate the leftmost index

        To know this, we need to understand the theory of a rotated array.

        A rotated array has two segments, a sorted side and an unsorted size with respect to the mid

        When we know we are in the sorted component we can return the lowest (This is when the left <= mid <= right)

        If from the beginning we always enter the unsorted component only while the left <= mid <= right is false, we will find the smallest rotated part

        this logic is true because there is a pivot index, the number that has been rotated where on oneside is the 
        the sorted space and the other an unsorted space about the pivot
        '''

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            left, right, mid = nums[l], nums[r], nums[m]
            print(left, mid, right)
            if left <= mid <= right:
                return left
            elif left <= mid:
                l = m + 1
            else:
                r = m
        return -1














