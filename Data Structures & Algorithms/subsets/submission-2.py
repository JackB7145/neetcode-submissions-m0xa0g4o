class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def traverse(idx):
            if idx >= len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[idx])
            traverse(idx+1)
            temp.pop()
            traverse(idx+1)
        
        traverse(0)
        return res