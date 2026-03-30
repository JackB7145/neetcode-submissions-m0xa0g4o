class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        key = defaultdict(int)
        for num in candidates: #Creating an index to know how many of 1 we can possibly have
            key[num] += 1
        
        res = []
        candidates = list(set(candidates)) #Getting rid of all the duplicates
        def recurse(subset, index):
            print(subset)
            nonlocal target #Accessing the nonlocal scope inside the solution method to access the target
            subset = subset.copy() #Copying the subset to prevent pointer and reference issues
            total = sum(subset) #Finding the sum of the subset 
            if total == target:
                res.append(subset)
            elif index < len(candidates) and total < target:
                for i in range(key[candidates[index]]+1):
                    recurse(subset+([candidates[index]]*i), index+1)
        
        recurse([], 0)
        return res