class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)):
            if nums[a] > 0:
                break  # optional: no way to reach 0 from here
            if a > 0 and nums[a] == nums[a-1]:
                continue

            l, r = a + 1, len(nums) - 1
            while l < r:
                total = nums[a] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # skipping l duplicates is enough; r will move on its own
        return res