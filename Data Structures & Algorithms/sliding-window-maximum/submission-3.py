class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        A brute force solution that is O(n^2) is easy to accomplish, just in chunks of 3, we find the minimum
        but for every window of size k, we would iterate over the items in the window n times for n numbers which creates the issue

        The issue I'm trying to resolve is, I need a way to find
        the last maximum, I'm thinking of using a monatomic stack as I iterate along

        say I have [2, 1, 3], At no point unless size 1 do I have to care about the middle number there so I can just input 2 and 3
        but even then removal will be an issue to remove numbers out of range

        The trick should be with the fact that it moves one at a time

        We have then situations to deal with.

        Basically then we should keep track of a last index as we iterate.

        That last index is the index of the maximum in the array

        wait, the lengh of the array is at most 1000, why can't we brute force it?
        '''


        res = []
        for i in range(len(nums)-k+1):
            print(f'({i}, {i+k})')
            res.append(max(nums[i:i+k]))
        
        return res