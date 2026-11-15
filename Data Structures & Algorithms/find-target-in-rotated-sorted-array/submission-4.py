class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            elif nums[l] <= nums[m] <= nums[r] and nums[l] <= target <= nums[r]:
                #Every iteration after this will be in a sorted region 
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1 

        return -1
