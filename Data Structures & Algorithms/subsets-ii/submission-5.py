class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(temp[:])
                return

            # Include the current element
            temp.append(nums[idx])
            backtrack(idx + 1)
            temp.pop()

            # Exclude the current element and skip duplicates
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1)

        backtrack(0)
        return res
