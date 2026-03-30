class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Each number represents a distance you can jump. If you can ake it to the end than you return true, otherwise you return false
        #You can jump to every index before the current 1
        if len(nums) <= 1:
            return True
        elif not nums[0]:
            return False
        distance = 0
        for i in range(len(nums)):
            print(i, distance)
            distance -= 1
            distance = max(distance, nums[i])
            if distance + i >= len(nums)-1:
                break
            while not nums[distance+i]:
                distance -= 1
            if distance == 0:
                return False
        return True