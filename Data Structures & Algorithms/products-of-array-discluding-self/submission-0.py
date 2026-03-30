class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1 for i in range(len(nums))]
        leftCounter = 1
        for i in range(len(nums)):
            temp[i] *= leftCounter
            leftCounter *= nums[i]
        rightCounter = 1
        for i in range(len(nums)-1, -1, -1):
            temp[i] *= rightCounter
            rightCounter *= nums[i]
        return temp
        

            
