class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        I can't swap at the end is the problem, as we might run over our edits

        I need to make an O(n) time complexity solution that solves this question in place.

        We need some kind of spacer with k

        where everything behind i is not a duplicate



        '''

        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            nums[k] = nums[i]
            k += 1

        return k