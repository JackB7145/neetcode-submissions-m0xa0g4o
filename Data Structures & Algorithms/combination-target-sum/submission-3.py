class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        used = set()
        def findPossibleCombinations(idx, total):
            if total == target:
                if tuple(temp[:]) not in used:
                    res.append(temp[:])
                    used.add(tuple(temp[:]))
                return

            elif idx >= len(nums) or total > target:
                return
            
            
            temp.append(nums[idx])
            findPossibleCombinations(idx, total + nums[idx])
            findPossibleCombinations(idx+1, total + nums[idx])
            temp.pop()
            findPossibleCombinations(idx+1, total)

        findPossibleCombinations(0, 0)
        return res