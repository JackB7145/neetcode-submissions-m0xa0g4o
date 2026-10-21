class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        c = 1
        for i in range(len(res)):
            res[i] *= c
            c *= nums[i]

        c = 1
        for i in range(len(res)-1, -1, -1):
            res[i] *= c
            c *= nums[i]
        
        return res