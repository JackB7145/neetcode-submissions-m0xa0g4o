class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(1, len(nums)):
            anchor = nums[i]
            if nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                
                total = anchor + nums[r] + nums[l] 
                if total == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

                if nums[l] == nums[l+1]:
                    l += 1
        
        return res

                
            
