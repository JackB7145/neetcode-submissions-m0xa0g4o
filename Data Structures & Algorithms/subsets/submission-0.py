class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generateSubsets(temp, i):
            if len(nums) <= i:
                res.append(temp[:])
                return
            temp.append(nums[i])
            generateSubsets(temp[:], i+1)
            temp.pop()
            generateSubsets(temp[:], i+1)
        
        generateSubsets([], 0)
        return res