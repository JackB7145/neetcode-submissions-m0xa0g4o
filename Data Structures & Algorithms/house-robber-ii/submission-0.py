class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHouses(start):
            rob1, rob2 = 0, 0
            for i in range(len(nums)-1):
                temp = max(nums[(start+i) % len(nums)] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        res = 0
        for i in range(len(nums)):
            res = max(robHouses(i), res)

        return res

        