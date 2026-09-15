class Solution:
    def rob(self, nums: List[int]) -> int:
        def findMaxRob(startIdx):
            one, two = 0, 0
            for i in range(len(nums)-1):
                currIdx = (startIdx+i)%len(nums)

                temp = one
                one = max(two+nums[currIdx], one)
                two = temp

            return one
        if len(nums) == 1:
            return nums[0]
        return max(findMaxRob(0), findMaxRob(1))