class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        res = 0
        while goal > 0:
            res += 1
            newStart = goal
            for i in range(goal-1, -1, -1):
                if nums[i] + i >= goal:
                    newStart = i
            goal = newStart

        return res
            