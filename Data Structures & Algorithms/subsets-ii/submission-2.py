class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        temp = []

        def traverse(idx):
            if idx >= len(nums):
                tup = tuple(list(sorted(temp[:])))
                if tup not in used:
                    res.append(temp[:])
                    used.add(tup)
                return
            
            temp.append(nums[idx])
            traverse(idx+1)
            temp.pop()
            traverse(idx+1)
        
        traverse(0)
        return res
    