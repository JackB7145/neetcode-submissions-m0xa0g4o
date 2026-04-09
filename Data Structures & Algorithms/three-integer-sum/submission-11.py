class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(f'Nums: {nums}')
        for i in range(0, len(nums)-3):
            anchor = nums[i]
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            print(i, l, r)
            while l < r:
                
                total = anchor + nums[r] + nums[l]
                print(f'total {total}') 
                if total == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return res

                
            
