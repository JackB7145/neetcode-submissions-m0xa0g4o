class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        The problem about this question is that its in place

        I could rotate an array easily with arr = arr[k:] + arr[:k]

        but the problem is we have to change the values not the indexes

        and in palace and I'm assuming without allocating any additonal space.

        If we wanted to do this brute force, we could rotate every element over once

        k times.


        so we could do it k * n times

        which is efficient but I think it can be done in O(N) thats why
        
        I want to start by doing it that way, as I'm not to confident of teh O(n) solution
    '''


        for _ in range(k):
            swap = nums[0]
            nums[0] = nums[-1]
            for i in range(1, len(nums)):
                temp = nums[i]
                nums[i] = swap
                swap = temp
                

