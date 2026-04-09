class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for a1 in range(len(nums)-3):
            if a1 > 0 and nums[a1] == nums[a1-1]:
                continue
            for a2 in range(a1+1, len(nums)-2):
                if a2 > a1+1 and nums[a2] == nums[a2-1]:
                    continue
                l, r = a2 + 1, len(nums)-1

                while l <= r:
                    while l > a2 + 1 and l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    temp = [nums[a1], nums[a2], nums[l], nums[r]]
                    total = sum(temp)
                    if total == target:
                        res.append(temp)
                        l+=1
                        r-=1
                    elif total < target:
                        l+=1
                    else:
                        r-=1

        return res
                    
                    