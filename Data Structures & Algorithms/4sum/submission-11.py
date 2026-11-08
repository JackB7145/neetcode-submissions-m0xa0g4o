class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a-1] == nums[a]:
                continue
            for b in range(a+1, len(nums)-2):
                if b > a + 1 and nums[b-1] == nums[b]:
                    continue

                l, r = b+1, len(nums)-1
                while l < r:
                    v1, v2, v3, v4 = nums[a], nums[b], nums[l], nums[r]
                    numbers = [v1, v2, v3, v4]
                    total = sum(numbers)

                    if total == target:
                        res.append(numbers)
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    
                    elif total < target:
                        l += 1
                    
                    else:
                        r -= 1
            
        return res