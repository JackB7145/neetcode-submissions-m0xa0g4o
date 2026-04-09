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

        for o(n)

        first we should identify what the swap should be 

        a swap that is 28 is the same as 28 % the length of the array, because then we
        start multi cycling right

        so we can do that

        then we look at 1 for instance, 1 can go to anywhere between 1 and the length of the array

        the problem is that we start overwriting after k elements in the array

        I can store a hashmap of these values in 2 loops, its not like it says do it in o(1) space complexity

        store everything after k. as a separate array? then iterate over it setting those values 

        but heres the issue we need to know where they came from
    '''



        k%=len(nums)
        # for _ in range(k):
        #     swap = nums[0]
        #     nums[0] = nums[-1]
        #     for i in range(1, len(nums)):
        #         temp = nums[i]
        #         nums[i] = swap
        #         swap = temp

        mp = nums[:k]
        print(mp)
        for i in range(k, len(nums)):
            
            idx = (i + k)%len(nums)
            print(f'Moving {nums[i]} to {idx}')
            nums[idx] = nums[i]
        
        for i in range(len(mp)):
            nums[i+k] = mp[i]


                

