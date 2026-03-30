class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        generate permutations, 
        but how do I get around duplicates.

        the issue in the permutations is that if you have

        [1123]

        Without removing duplicates

        
         [1]                        [1]                        [2]                        [3]
  [1,1] [1,2] [1,3]

        '''

        res = []
        nums.sort()
        used = [False for _ in range(len(nums))] 
        def traverse(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if 0 < i and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                curr.append(nums[i])
                traverse(curr)
                curr.pop()
                used[i] = False
        traverse([])
        return res
                
                


            