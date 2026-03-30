class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def findPossibleCombinations(idx, total):
            if total == target:
                res.append(temp[:])
                return

            elif idx >= len(nums) or total > target:
                return
            
            
            temp.append(nums[idx])
            findPossibleCombinations(idx, total + nums[idx])
            temp.pop()
            findPossibleCombinations(idx+1, total)

        findPossibleCombinations(0, 0)
        return res