class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        So you either can take the n-1 or n + n-2
        '''

        one, two = 0, 0

        for i in range(len(nums)):
            temp = one
            one = max(two+nums[i], one)
            two = temp

        return one