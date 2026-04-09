class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Each number represents a distance you can jump. If you can ake it to the end than you return true, otherwise you return false
        #You can jump to every index before the current 1

        if len(nums) <= 1:
            return True
        elif not nums[0]:
            return False
        for i in range(len(nums)):
            distance = nums[i]
            print(i, distance)
            if not distance:
                continue
            elif i + distance + 1 >= len(nums):
                return True
            while not nums[i+distance]:
                distance -= 1
            if distance == 0:
                return False