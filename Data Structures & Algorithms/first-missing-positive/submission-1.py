class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue

            index = nums[i] - 1
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        '''
        This works because we know that if we have an array of size 7 for example, that the number must be between 1 - 7, the best possible scenario

        is 1, 2, 3, 4 ... 7 right, which the answer is 8. Any diversion from that will just make the number less than 8. 

        We don't consider any numbers negative and greater than the length, and then after, go through and look for the element that doesn't align with
        its index. that is the number. 

        '''