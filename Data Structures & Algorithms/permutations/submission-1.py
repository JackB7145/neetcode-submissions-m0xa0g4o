class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutations(path, check):
            path = path.copy()
            check = check.copy()
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if check[i]:
                    path.append(nums[i])
                    check[i] = False
                    permutations(path, check)
                    path.pop()
                    check[i] = True
                    

        permutations([], [True for _ in range(len(nums))])

        return res
        
        
    