class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(temp[:])
                return

            # Include current element
            temp.append(nums[idx])
            backtrack(idx + 1)
            temp.pop()

            # Exclude current element and skip duplicates
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx-1]:
                idx += 1
            backtrack(idx)

        backtrack(0)
        return res
