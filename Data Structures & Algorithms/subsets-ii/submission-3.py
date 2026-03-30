class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(temp[:])
                return
            
            # Include nums[idx]
            temp.append(nums[idx])
            backtrack(idx + 1)
            temp.pop()

            # Skip duplicates for the "exclude" path
            next_idx = idx + 1
            while next_idx < len(nums) and nums[next_idx] == nums[idx]:
                next_idx += 1
            backtrack(next_idx)

        backtrack(0)
        return res
