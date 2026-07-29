class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        seen = [False for _ in range(len(nums))]
        def permute():
            if len(temp) == len(nums):
                res.append(temp[:])
                return

            for idx in range(len(nums)):
                if idx > 0 and seen[idx-1] == False and nums[idx] == nums[idx-1]:
                    continue
                if not seen[idx]:
                    seen[idx] = True
                    temp.append(nums[idx])
                    permute()
                    seen[idx] = False
                    temp.pop()

        permute()
        return res