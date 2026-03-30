class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(subset, index):
            #We make a recursive call for the maximum number of times the number at index can go into the target target // nums[index]
            #We include one call where we don't include it
            nonlocal target
            subset = subset.copy()
            total = sum(subset)
            if total == target:
                res.append(subset)
            elif index < len(nums) and total < target:
                ourNumber = nums[index]
                for i in range(target//ourNumber+1):
                    recurse(subset+([ourNumber]*i), index+1)
                
        recurse([], 0)
        return res