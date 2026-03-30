class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def permute(idx):
            nonlocal res, temp
            if idx >= len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[idx])
            permute(idx+1)
            temp.pop()
            permute(idx+1)
        
        permute(0)
        return res
